from django.db import models

# Create your models here.

class Users(models.Model):
    first_name=models.CharField(max_length=100,blank=False,)
    last_name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Student(models.Model):
    name=models.CharField(max_length=100,)
    mobile=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    DOB=models.DateField(blank=False)

    def __str__(self):
        return self.name
