from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.


class Contact(models.Model):

    email = models.EmailField()
    message = models.TextField()