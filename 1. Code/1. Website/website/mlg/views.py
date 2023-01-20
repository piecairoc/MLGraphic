from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateUser
from .models import Users

# Create your views here.


def index(response):
    return render(response, 'mlg/base.html', {})


def home(response):
    return render(response, 'mlg/home.html', {"name": '1'})


def user(response, id):
    us = Users.objects.get(id=id)
    return render(response, 'mlg/user.html', {"us": us})

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