from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title