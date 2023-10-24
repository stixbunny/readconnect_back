from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Author, Category, Review, ReadList, ToReadList

admin.site.register(User, UserAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(ReadList)
admin.site.register(ToReadList)