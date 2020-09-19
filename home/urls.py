
from django.contrib import admin
from django.urls import path, include
from . import views


admin.site.site_header = "Shimul's ToDo"
admin.site.site_title = "Welcome to ToDo list"
admin.site.index_title  = "Welcome to  this Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tasks',  views.tasks, name = 'tasks')
]
