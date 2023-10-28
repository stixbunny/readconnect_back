import graphene
from .models import User, Book, Author, Category, Review, ReadList, ToReadList
from .types import BookType, AuthorType, CategoryType


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    all_categories = graphene.List(CategoryType)
    book_by_title = graphene.Field(
        BookType, title=graphene.String(required=True)
    )
    author_by_name = graphene.Field(
        AuthorType, name=graphene.String(required=True)
    )
    category_by_name = graphene.Field(
        CategoryType, name=graphene.String(required=True)
    )

    def resolve_all_books(root, info):
        return Book.objects.prefetch_related("authors", "categories").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.prefetch_related("books").get(name=name)
        except Category.DoesNotExist:
            return None
    
    def resolve_author_by_name(root, info, name):
        # if not info.context.user.is_authenticated:
        #     return None
        try:
            return Author.objects.prefetch_related("books").get(name=name)
        except Author.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
