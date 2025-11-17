from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def test_view(request):
    return JsonResponse({'message': 'API is working!'})

def home(request):
    return HttpResponse("Welcome to the Podcast Platform!")

def test_view(request):
    return HttpResponse("This is a test view!")