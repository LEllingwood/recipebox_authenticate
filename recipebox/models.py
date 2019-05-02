from django.db import models
from django.contrib.auth.models import User


# all classes go here
class Author(models.Model):
    name = models.CharField(max_length=50)
    user = models.OnetoOne(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return  self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCASE)
    description = models.CharField(max_length=100, null=True, blank=True)
    time_required = models.TimeField(null=True, blank=True)
    instructions = models.TextField()

    