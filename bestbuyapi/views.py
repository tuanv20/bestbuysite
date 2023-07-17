from django.shortcuts import render
from django.http import JsonResponse
import requests as reqs

# Create your views here.
def getLaptops(request):
    params = {
        'apiKey': 'qhqws47nyvgze2mq3qx4jadt',
        'format': 'json',
    }
    #print(request.GET['keyword'])  
    #if(request.GET['keyword'] == 'laptop'):
    response = reqs.get('https://api.bestbuy.com/v1/products((categoryPath.id=abcat0502000))', params=params)   
    print(response.json())
    return JsonResponse(response.json())

