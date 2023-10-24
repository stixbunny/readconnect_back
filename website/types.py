from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from .models import User, Book, Author, Category, Review, ReadList, ToReadList


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        filter_fields = {
            "id": ["exact"],
            "title": ["exact", "icontains", "istartswith"],
            "isbn": ["exact", "istartswith"],
            "page_count": ["lt", "gt"],
            "published_date": ["exact", "year__lt", "year__gt"],
            "authors": ["exact"],
            "categories": ["exact"],
            "reviews": ["exact"],
        }
        interfaces = (relay.Node,)

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.prefetch_related("authors", "categories")


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ["id", "name"]
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        return Category.objects.get(pk=id)


class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = ["id", "name"]
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info, id):
        return Author.objects.get(pk=id)
