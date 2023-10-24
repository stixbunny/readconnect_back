from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=15, blank=True)
    page_count = models.SmallIntegerField()
    published_date = models.DateField(null=True, blank=True)
    img = models.URLField(blank=True)
    short_description = models.TextField(max_length=2000, blank=True)
    long_description = models.TextField(max_length=3000, blank=True)
    authors = models.ManyToManyField("Author")
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(AbstractUser):
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    reviews = models.ManyToManyField(to=Book, through="Review")

    def __str__(self):
        return self.username


class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)

    RATING_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    rating = models.SmallIntegerField(choices=RATING_CHOICES)
    description = models.TextField(max_length=1000)

    class Meta:
        unique_together = ["user", "book"]

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


class ReadList(models.Model):
    user = models.ForeignKey(to=User, related_name="booksread", on_delete=models.CASCADE)
    booklist = models.ManyToManyField(to=Book)
    
    def __str__(self):
        return f"{self.user.username}'s read list"


class ToReadList(models.Model):
    user = models.ForeignKey(to=User, related_name="bookstoread", on_delete=models.CASCADE)
    booklist = models.ManyToManyField(to=Book)
    
    def __str__(self):
        return f"{self.user.username}'s to read list"
