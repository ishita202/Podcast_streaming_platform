from django.urls import path
from . import views

app_name = 'podcasts'  # Keep the namespace declaration

urlpatterns = [
    path('', views.podcast_list, name='podcast_list'),
    path('<int:id>/', views.podcast_detail, name='podcast_detail'),
    path('upload/', views.upload_podcast, name='upload_podcast'),  # Only need this once
    path('stream/<int:id>/', views.stream_podcast, name='stream_podcast'),
]