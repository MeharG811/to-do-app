from django.urls import path,include
from .views import *
from django.contrib import admin
from .models import Tasks


urlpatterns = [
    path("", home, name='home'),
    path('edit_task/<int:id>/', edit_task, name='edit_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
]

admin.site.register(Tasks)