import json
from datetime import datetime

authors_id = 1
categories_id = 1

authors = []
categories = []


def contains(list, name):
    result = [member for member in list if member["fields"]["name"] == name]
    if result:
        return result[0]["pk"]
    else:
        return 0


def addAuthor(name):
    global authors_id
    global authors
    id = contains(authors, name)
    if id == 0:
        id = authors_id
        authors.append(newAuthor(name))
        return id
    else:
        return id


def newAuthor(name):
    global authors_id
    author = {}
    author["model"] = "website.author"
    author["pk"] = authors_id
    author["fields"] = {}
    author["fields"]["name"] = name
    authors_id += 1
    return author


def addCategory(name):
    global categories
    global categories_id
    id = contains(categories, name)
    if id == 0:
        id = categories_id
        categories.append(newCategory(name))
        return id
    else:
        return id


def newCategory(name):
    global categories_id
    category = {}
    category["model"] = "website.category"
    category["pk"] = categories_id
    category["fields"] = {}
    category["fields"]["name"] = name
    categories_id += 1
    return category


def main():
    global authors
    global categories
    new_books = []
    with open("books.json") as file:
        books = json.load(file)
    for id, book in enumerate(books, start=1):
        new_book = {}
        new_book["model"] = "website.book"
        new_book["pk"] = id
        new_book["fields"] = {}
        new_book["fields"]["title"] = book["title"]
        new_book["fields"]["page_count"] = book["pageCount"]
        new_book["fields"]["authors"] = []
        if "authors" in book and len(book["authors"]) > 0:
            for author in book["authors"]:
                if author != "":
                    new_book["fields"]["authors"].append(addAuthor(author))
        new_book["fields"]["categories"] = []
        if "categories" in book and len(book["categories"]) > 0:
            for category in book["categories"]:
                new_book["fields"]["categories"].append(addCategory(category))
        if "isbn" in book:
            new_book["fields"]["isbn"] = book["isbn"]
        if "publishedDate" in book:
            new_book["fields"]["published_date"] = (
                datetime.fromisoformat(book["publishedDate"]["$date"]).date().isoformat()
            )
        if "thumbnailUrl" in book:
            new_book["fields"]["img"] = book["thumbnailUrl"]
        if "shortDescription" in book:
            new_book["fields"]["short_description"] = book["shortDescription"]
        if "longDescription" in book:
            new_book["fields"]["long_description"] = book["longDescription"]
        new_books.append(new_book)
    json_objects = (
        [author for author in authors]
        + [category for category in categories]
        + [b for b in new_books]
    )
    with open("fixture.json", "w") as file:
        json.dump(
            json_objects, file, indent=4, sort_keys=False, ensure_ascii=False
        )


if __name__ == "__main__":
    main()
