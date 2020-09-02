from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20, null=True)
    author = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=20, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
