from django.db import models
from django.utils import timezone


"""
------------- Aim --------------
Create Users objects to identify the user of the program

---------- Parameters ----------
(TYPE)       | NAME         | DESCRIPTION
(str)        | firstname    | (optional) First name of the user
(str)        | lastname     | (optional) Last name of the user
(str)        | pseudo       | Username of the User
(str)        | password     | Password
"""
class Users(models.Model):
    firstname = models.CharField(max_length = 200)
    lastname  = models.CharField(max_length = 200)
    pseudo    = models.CharField(max_length = 200)
    password  = models.CharField(max_length = 200)

    def __str__(self):
        return self.firstname


"""
------------- Aim --------------
Create Projects related to one User.

---------- Parameters ----------
(TYPE)       | NAME                     | DESCRIPTION
(Users)      | user                     | User who owns the Project
(str)        | name                     | Name of the project
(str)        | comment                  | (optional) Comment left by the user
(dateField   | date_last_modification   | Date of the latest modification of the model
"""
class Projects(models.Model):
    user                   = models.ForeignKey(Users, on_delete = models.CASCADE)
    name                   = models.CharField(max_length = 200)
    comment                = models.CharField(max_length = 1000)
    date_creation          = models.DateField(default=timezone.now)
    date_last_modification = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


"""
------------- Aim --------------
Create Users objects to identify the user of the program

---------- Parameters ----------
(TYPE)       | NAME       | DESCRIPTION
(Project)    | project    | 
(str)        | name       | 
(int)        | repeat     | 
(bool)       | ignore     | 
"""
class Actions(models.Model):
    project = models.ForeignKey(Projects, on_delete = models.CASCADE)
    name    = models.CharField(max_length = 200)
    repeat  = models.IntegerField(default = 1)
    ignore  = models.BooleanField(default = False)

    def __str__(self):
        return self.name


"""
------------- Aim --------------
Create Users objects to identify the user of the program

---------- Parameters ----------
(TYPE)       | NAME       | DESCRIPTION
(Project)    | project    | 
(str)        | name       | 
(int)        | repeat     | 
(bool)       | ignore     | 
"""
class Parameters(models.Model):
    action  = models.ForeignKey(Actions, on_delete = models.CASCADE)
    key     = models.CharField(max_length = 200)
    value   = models.CharField(max_length = 200)
    comment = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.key