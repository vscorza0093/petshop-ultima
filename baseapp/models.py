from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()


class PetShower(models.Model):
    petname = models.CharField(max_length=50)
    ownername = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=11)
    bookingdate = models.DateTimeField(auto_now_add=False)
    petsize = models.CharField(max_length=1)
    observations = models.TextField()


class PetToy(models.Model):
    toyname = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
