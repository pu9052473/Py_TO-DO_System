from pickle import FALSE
from djongo import models
from django.contrib.auth.hashers import check_password as django_check_password

# Create your models here.


class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=500, null=False)
    lastName = models.CharField(max_length=500, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=500, null=False)
    def check_password(self, raw_password):
        """ Check the password against the user's password hash. Returns True if the password is valid, or False otherwise. """
        return django_check_password(raw_password, self.password)

class Todos(models.Model):
    todoID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=500, null=False)
    dueDate = models.DateField(null=False)
    completed = models.BooleanField(default=False, null=False)