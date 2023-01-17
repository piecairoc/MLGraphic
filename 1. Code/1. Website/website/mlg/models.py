from django.db import models

# Create your models here.

class Users(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname  = models.CharField(max_length = 200)
    password  = models.CharField(max_length = 200)

    def __str__(self):
        return self.firstname



class Actions(models.Model):
    name   = models.CharField(max_length = 200)
    repeat = models.IntegerField(default = 1)
    ignore = models.BooleanField(default = False)

class Parameters(models.Model):
    action = models.ForeignKey(Actions, on_delete = models.CASCADE)
    key    = models.CharField(max_length = 200)
    value  = models.CharField(max_length = 200)