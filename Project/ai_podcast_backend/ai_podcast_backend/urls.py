from django.contrib import admin
from django.urls import path, include
from authentication.views import welcome_view
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Home view displaying useful links
def home_view(request):
    return HttpResponse("""
        <h1>Welcome to the Podcast Platform!</h1>
        <p>Explore the platform: </p>
        <ul>
            <li><a href="/auth/signup/">Signup</a></li>
            <li><a href="/auth/login/">Login</a></li>
            <li><a href="/admin/">Admin Panel</a></li>
        </ul>                
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='authentication')),
    path('podcasts/', include('podcasts.urls', namespace='podcasts')),  # Keep only ONE podcast route
    path('subscriptions/', include('subscriptions.urls')),
    path('api/recommendations/', include('recommendations.urls')),
    path('api/', include('api.urls')),
    path('', welcome_view, name='welcome'),
    path('home/', home_view, name='home'),
]

# Serve media files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
