from graphene_django import DjangoObjectType
from .models import User, Book, Author, Category, Review, ReadList, ToReadList


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "isbn",
            "page_count",
            "published_date",
            "img",
            "short_description",
            "long_description",
            "authors",
            "categories",
            "reviews",
            "inreadlist",
            "intoreadlist",
        )


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name", "books")


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name", "books")
