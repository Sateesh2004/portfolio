from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    number=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=500)