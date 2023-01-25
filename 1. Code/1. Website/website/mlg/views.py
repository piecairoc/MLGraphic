from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateUser
from .models import Users, Projects
from datetime import datetime



"""
------------- Aim --------------
Create a webpage to welcome the users

---------- Parameters ----------
(TYPE)       | NAME        | DESCRIPTION
(unknown)    | response    | Webpage
"""
def index(response):
    return render(response, 'mlg/base.html', {})



"""
------------- Aim --------------
Create a homepage to welcome the users

---------- Parameters ----------
(TYPE)       | NAME       | DESCRIPTION
(unknown)    | response   | Webpage
"""
def home(response):
    return render(response, 'mlg/home.html', {"name": '1'})



"""
------------- Aim --------------
Create a webpage to display the User's info and projects

---------- Parameters ----------
(TYPE)       | NAME       | DESCRIPTION
(unknown)    | response   | Webpage
(int)        | id         | User ID
"""
def user(response, id):
    us = Users.objects.get(id=id)
    print(us.projects_set.all())

    if response.method == 'POST':
        if response.POST.get('createProject'):
            txt = response.POST.get('projectName')
            print(txt)
            if len(txt) > 2:
                us.projects_set.create(name=txt, comment='')
            else:
                print('Name too short')

    return render(response, 'mlg/user.html', {"us": us})



"""
------------- Aim --------------
Create a webpage to display the elements of the current project

---------- Parameters ----------
(TYPE)       | NAME       | DESCRIPTION
(unknown)    | response   | Webpage
(int)        | id         | User ID
"""
def project(response, id):
    us = Projects.objects.get(id=id)
    print(us.actions_set.all())

    if response.method == 'POST':
        if response.POST.get('createProject'):
            txt = response.POST.get('projectName')
            print(txt)
            if len(txt) > 2:
                us.actions_set.create(name=txt, comment='')
            else:
                print('Name too short')

    return render(response, 'mlg/user.html', {"us": us})



"""
------------- Aim --------------
Create Users objects to identify the user of the program

---------- Parameters ----------
(TYPE)       | NAME       | DESCRIPTION
(unknown)    | response   | Webpage
"""
def create(response):
    if response.method == 'POST':
        form = CreateUser(response.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname  = form.cleaned_data['lastname']
            pseudo    = form.cleaned_data['pseudo']
            password  = form.cleaned_data['password']
            u = Users(firstname = firstname, lastname = lastname, pseudo = pseudo, password = password)
            u.save()
        return HttpResponseRedirect('/%i' %u.id)
    else:
        form = CreateUser()
    return render(response, 'mlg/create.html', {"form": form})