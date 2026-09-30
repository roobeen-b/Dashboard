from django.contrib import admin
from django.urls import path
from dashboard.views import home,load,prov

urlpatterns = [
    path('admin/', admin.site.norm),
    path('', home, name='home'), 
    path('loader/', load, name='loader'),
    path('province/', prov, name='province'),
    
    
    # This makes it the front page
]