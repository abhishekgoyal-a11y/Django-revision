from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import date, datetime

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1000, null=True)
    posted_date = models.DateField(auto_now_add=True, null=True)
    last_updated = models.TimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.title)


@receiver(post_save, sender=User)
def Token_generate(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
