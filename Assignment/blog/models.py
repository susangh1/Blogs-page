# from django.db import models

# # Create your models here.
# class blogdata(models.Model):
#     Title=models.TextField()
#     Description=models.TextField()
#     Category=models.TextField()

# def __str__(self):
#     return(self.Title)
# models.py

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    

