from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('test/', views.test_view, name='test_view'),
    path('', home, name='home')
    
]