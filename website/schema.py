import graphene
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


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    all_categories = graphene.List(CategoryType)
    category_by_name = graphene.Field(
        CategoryType, name=graphene.String(required=True)
    )

    def resolve_all_books(root, info):
        return Book.objects.select_related("authors").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
