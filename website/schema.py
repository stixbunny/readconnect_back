from graphene import relay, ObjectType, List as GrapheneList
from graphene_django.filter import DjangoFilterConnectionField
from .types import BookNode, AuthorNode, CategoryNode
from .models import Author, Category


class Query(ObjectType):
    book = relay.Node.Field(BookNode)
    all_books = DjangoFilterConnectionField(BookNode)
    author = relay.Node.Field(AuthorNode)
    # all_authors = GrapheneList(AuthorNode)
    category = relay.Node.Field(CategoryNode)
