from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('<int:id>', views.model, name='model'),
    path('create/', views.create, name='create'),
]