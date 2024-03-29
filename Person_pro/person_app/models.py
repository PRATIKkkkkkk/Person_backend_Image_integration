from django.db import models


class Person(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    profile_pic = models.ImageField(upload_to='profile_pictures/')
    email = models.EmailField()
    city = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)