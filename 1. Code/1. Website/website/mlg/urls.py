from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('<int:id>', views.user, name='user'),
    path('create/', views.create, name='create'),
    path('project/<int:id>', views.project, name="project")
]