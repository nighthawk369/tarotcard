from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from tarotapp.models import TarotCard
from rest_framework.views import APIView
from .serializers import TarotSerializer
from random import randint
from django.shortcuts import render
import json

class list(APIView):
    num=randint(0,77)
    def get(self, request):
        num=randint(0,77)
        queryset = TarotCard.objects.filter(number=num)
        serializer = TarotSerializer(queryset, many=True)
        return Response(serializer.data)


def home(request):
    context={
        "data": TarotCard.objects.filter(number=23)
    }
    return render(request,'home.html',context)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def reading(request):
    return render(request,'reading.html')


def reiki(request):
    return render(request,'reiki.html')

def astrology(request):
    return render(request,'astrology.html')

# def glist(request):
#     nikhil={
#     "name": "John Doe",
#     "age": "30",
#     "email": "john.doe@example.com",
#     "city": "New York",
#     "isStudent": "false"
#     }

#     return JsonResponse(nikhil)


def glist(request):
    num=randint(0,77)
    data = TarotCard.objects.filter(number=num)
    for i in data:
        number=i.number
        name=i.name
        image_url=i.image_url
        meaning=i.meaning

    nikhil={
        "number":f"{number}",
        "name":f"{name}",
        "image_url":f"{image_url}",
        "meaning":f"{meaning}"
    }
    return JsonResponse(nikhil)