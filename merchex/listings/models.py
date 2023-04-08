from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)

class Listing(models.Model):
    title = models.fields.CharField(max_length=100)

class Contact(models.Model):
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(max_length=100)
    number = models.fields.CharField(max_length=10)
    mail = models.fields.CharField(max_length=100)