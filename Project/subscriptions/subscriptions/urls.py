from django.urls import path
from .views import select_subscription, subscription_history, user_subscription_plans, subscription_home
from django.urls import path
from . import views

urlpatterns = [
    path('plans/', user_subscription_plans, name='user_subscription_plans'),
    path('select/', select_subscription, name='select_subscription'),
    path('history/', subscription_history, name='subscription_history'),
    path("home/", views.subscription_home, name="subscription_home"),


]
