from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_category = models.CharField(max_length=100)
    book_price = models.IntegerField()

    def __str__(self):
        return self.book_name