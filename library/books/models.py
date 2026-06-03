from django.db import models

class Author(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    age = models.IntegerField()

    books_count = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    date_published = models.DateField()

    isbn = models.CharField(max_length=13)