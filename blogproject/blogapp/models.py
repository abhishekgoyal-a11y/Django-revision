from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.TextField(max_length=200, null=True)
    message = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return str(self.title)
