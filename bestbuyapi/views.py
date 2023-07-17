from django.shortcuts import render
from django.http import JsonResponse
import requests as reqs
import json

# Create your views here.
def getlaptops(request):
    params = {
        'apiKey': 'qhqws47nyvgze2mq3qx4jadt',
        'format': 'json',
    }

    response = reqs.get('https://api.bestbuy.com/v1/products((categoryPath.id=abcat0502000))', params=params)   
    # productDict = json.loads(response.text)["products"]
    # out = [x["name"] for x in productDict]
    # test = json.loads(json.dumps(productDict))
    return JsonResponse(response.json())

