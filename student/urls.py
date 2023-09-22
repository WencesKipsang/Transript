from django.urls import path,include
from .views import *

urlpatterns = [
    path('adminhome/', admin_home,name= "home"),
    path('addunit/', add_unit, name= "add_unit"),
    path('addcourses/', add_course, name= "addcourse"),
    path('chart/', chart, name= "viewchart"),
]