from pickle import FALSE
from djongo import models

# Create your models here.

class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=500, null=False)
    lastName = models.CharField(max_length=500, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=500, null=False)

class Todos(models.Model):
    todoID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=False)
    dueDate = models.DateField(null=False)
    completed = models.BooleanField(default=False, null=False)