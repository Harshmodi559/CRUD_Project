from turtle import update
from django.contrib import admin
from django.urls import path
from requests import delete
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls,name="admin"),
    path('',views.home,name="home"),
    path('delete/<int:id>',views.delete_data,name="delete"),
    path('update/<int:id>',views.update_data,name="update")
]