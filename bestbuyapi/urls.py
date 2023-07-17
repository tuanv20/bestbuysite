from django.urls import path 
from . import views

urlpatterns = [
    #Always end an endpoint with a / 
    path('laptops/', views.getLaptops)
]