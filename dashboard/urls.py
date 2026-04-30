from django.contrib import admin
from django.urls import path
from dashboard.views import home,load

urlpatterns = [
    path('admin/', admin.site.norm),
    path('', home, name='home'), 
    path('loader/', load, name='loader'),
    
    # This makes it the front page
]