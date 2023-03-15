from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
import json

from .models import Smartphones, Details


def get_product(request: HttpRequest) -> JsonResponse:
    smartphones = Smartphones.objects.all()
    data = []

    for smartphone in smartphones:
        data.append(
            {
                'name': smartphone.name,
                'model': smartphone.model,
                'price': smartphone.price,
                'img_url': smartphone.img_url,
                'color': smartphone.details.color,
                'ram': smartphone.details.ram,
                'memory': smartphone.details.memory
            }
        )
    response = {
        "result": data
    }

    return JsonResponse(response)

def add_product(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        bdy = request.body
        dcd = bdy.decode()
        data = json.loads(dcd)

        color = data.get('color')
        ram = data.get('ram')
        memory = data.get('memory')

        price = data.get('price')
        img_url = data.get('img_url')
        name = data.get('name')
        model = data.get('model')

        if price == None:
            return JsonResponse({"status": "price field is required."})
        if img_url == None:
            return JsonResponse({"status": "img_url field is required."})
        if color == None:
            return JsonResponse({"status": "color field is required."})
        if ram == None:
            return JsonResponse({"status": "ram field is required."})
        if memory == None:
            return JsonResponse({"status": "memory field is required."})
        if name == None:
            return JsonResponse({"status": "name field is required."})
        if model == None:
            return JsonResponse({"status": "model field is required."})

        detail = Details()
        detail.color = color
        detail.memory = memory
        detail.ram = ram
        detail.save()

        smartphone = Smartphones()
        smartphone.name = name
        smartphone.model = model
        smartphone.price = price
        smartphone.img_url = img_url
        smartphone.details = Details.objects.all().last()
        smartphone.save()

        return JsonResponse({"result":data})
    
def get_with_model(request: HttpRequest, model):
    smartphones = Smartphones.objects.filter(model__icontains=model)
    data = []

    for smartphone in smartphones:
        data.append(
            {
                'name': smartphone.name,
                'model': smartphone.model,
                'price': smartphone.price,
                'img_url': smartphone.img_url,
                'color': smartphone.details.color,
                'ram': smartphone.details.ram,
                'memory': smartphone.details.memory
            }
        )
    response = {
        "result": data
    }

    return JsonResponse(response)


def get_with_price_gt(request: HttpRequest, gt): 
    smartphones = Smartphones.objects.filter(price__gt=gt).order_by('price')
    data = []

    response = {
        "result": data
    }

    for smartphone in smartphones:
        data.append(
            {
                'name': smartphone.name,
                'model': smartphone.model,
                'price': smartphone.price,
                'img_url': smartphone.img_url,
                'color': smartphone.details.color,
                'ram': smartphone.details.ram,
                'memory': smartphone.details.memory
            }
        )
    
    return JsonResponse(response)

def get_with_price_lt(request: HttpRequest, lt): 
    smartphones = Smartphones.objects.filter(price__lt=lt).order_by('price')
    data = []

    response = {
        "result": data
    }

    for smartphone in smartphones:
        data.append(
            {
                'name': smartphone.name,
                'model': smartphone.model,
                'price': smartphone.price,
                'img_url': smartphone.img_url,
                'color': smartphone.details.color,
                'ram': smartphone.details.ram,
                'memory': smartphone.details.memory
            }
        )
    
    return JsonResponse(response)