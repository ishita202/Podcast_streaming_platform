from django.contrib import admin
from django.urls import path, include
from authentication import views as auth_views #Import views for homepage

urlpatterns= [
    path('admin/', admin.site.urls),
    path('', auth_views.home_views, name='home'), #homepage
    path('auth/', include('authentication.urls')), #includes authentication URls
]