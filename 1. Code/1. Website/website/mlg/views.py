from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return render(response, 'mlg/base.html', {})


def home(response):
    return render(response, 'mlg/home.html', {"name": '1'})


def model(response, id):
    # ls = ToDoList.objects.get(id=id)
    return render(response, 'mlg/home.html', {"name": str(id)})