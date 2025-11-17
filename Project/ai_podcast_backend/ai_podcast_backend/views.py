from django.http import JsonResponse
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return JsonResponse({"message": "Welcome to the Podcast API"})

from django.contrib.auth.models import User
from django.views import View

class RegisterView(View):
    def post(self, request):
        return JsonResponse({"message": "User registered successfully!"})
    
class LoginView(DjangoLoginView):
    template_name= 'login.html'

def home(request):
    return HttpResponse("Welcome to the Podcast Platform!")

@login_required
def home_view(request):
    return render(request, 'home.html')

def welcome_view(request):
    return render(request, 'authentication/welcome.html') 

def login_view(request):
    return render(request, 'authentication/login.html')
