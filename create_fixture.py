import json
from datetime import datetime

authors_id = 1
categories_id = 1

authors = []
categories = []


def contains(list, name):
    result = [member for member in list if member["name"] == name]
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
    author["name"] = name
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
    category["name"] = name
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
        new_book["title"] = book["title"]
        new_book["page_count"] = book["pageCount"]
        new_book["authors"] = []
        if "authors" in book and len(book["authors"]) > 0:
            for author in book["authors"]:
                new_book["authors"].append(addAuthor(author))
        new_book["categories"] = []
        if "categories" in book and len(book["categories"]) > 0:
            for category in book["categories"]:
                new_book["categories"].append(addCategory(category))
        if "isbn" in book:
            new_book["isbn"] = book["isbn"]
        if "publishedDate" in book:
            new_book["published_date"] = (
                datetime.fromisoformat(book["publishedDate"]["$date"])
                .now()
                .isoformat()
            )
        if "thumbnailUrl" in book:
            new_book["img"] = book["thumbnailUrl"]
        if "shortDescription" in book:
            new_book["short_description"] = book["shortDescription"]
        if "longDescription" in book:
            new_book["long_description"] = book["longDescription"]
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
