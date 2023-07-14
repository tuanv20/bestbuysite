from django.shortcuts import render
from django.http import JsonResponse
import requests as reqs

# Create your views here.
def getlaptops(request):
    params = {
        'apiKey': 'qhqws47nyvgze2mq3qx4jadt',
        'format': 'json',
    }

    response = reqs.get('https://api.bestbuy.com/v1/products((categoryPath.id=abcat0502000))', params=params)
    return JsonResponse(response.json())

