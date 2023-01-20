from django.db import models

# Create your models here.

class Users(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname  = models.CharField(max_length = 200)
    pseudo    = models.CharField(max_length = 200)
    password  = models.CharField(max_length = 200)

    def __str__(self):
        return self.firstname

class Projects(models.Model):
    user                   = models.ForeignKey(Users, on_delete = models.CASCADE)
    name                   = models.CharField(max_length = 200)
    comment                = models.CharField(max_length = 1000)
    date_last_modification = models.DateField()

    def __str__(self):
        return self.name

class Actions(models.Model):
    project = models.ForeignKey(Projects, on_delete = models.CASCADE)
    name    = models.CharField(max_length = 200)
    repeat  = models.IntegerField(default = 1)
    ignore  = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Parameters(models.Model):
    action  = models.ForeignKey(Actions, on_delete = models.CASCADE)
    key     = models.CharField(max_length = 200)
    value   = models.CharField(max_length = 200)
    comment = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.key