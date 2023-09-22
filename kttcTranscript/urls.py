
from django.contrib import admin
from django.urls import path,include
from student import urls as hey

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(hey)),
]
