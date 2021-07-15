from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Client
# Create your views here.
def register(request):
    c = Client.objects.all()

    print(c)
    return JsonResponse({})