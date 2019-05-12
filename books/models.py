from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=800)
    puce = models.CharField(max_length=30)