from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser
import logging

logger = logging.getLogger(__name__)

User = get_user_model()


def user_signup(request):
    if request.user.is_authenticated and not request.user.is_staff:
        messages.info(request, "You are already signed in.")
        return redirect('authentication:home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  
            user.save()
            messages.success(request, "Signup successful! Please log in.")
            return redirect('authentication:login')
        else:
            messages.error(request, "Signup failed. Please check the form.")
            print(form.errors)  # Debugging

    else:
        form = CustomUserCreationForm()

    return render(request, 'authentication/signup.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated and not request.user.is_staff:
        logger.info(f"User already authenticated: {request.user}")
        return redirect('authentication:home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']  # ✅ Match form field name
            password = form.cleaned_data['password']

            print(f"Trying to authenticate user: {username_or_email}")  # Debugging
            user = authenticate(request, username=username_or_email, password=password)

            if user is not None:
                print(f"Authenticated user: {user}")  # Debugging
                logger.info(f"User authenticated successfully: {user}")
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('authentication:home')
            else:
                print(f"Authentication failed for: {username_or_email}")  # Debugging
                logger.warning(f"Authentication failed for user: {username_or_email}")
                messages.error(request, "Invalid email or password. Please try again.")  # ✅ Used messages.error()
        else:
            logger.warning("Form validation failed")
            messages.error(request, "Invalid form submission.")

    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form': form})  # ✅ Removed unnecessary 'error' variable


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('authentication:login')


def home_view(request):
    return render(request, 'authentication/home.html')


def welcome_view(request):
    return render(request, 'authentication/welcome.html')
