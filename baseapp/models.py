from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
