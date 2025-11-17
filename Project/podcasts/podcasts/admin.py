from django.contrib import admin
from .models import Podcast

@admin.register(Podcast)  # This automatically registers Podcast with PodcastAdmin
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_by', 'uploaded_at']
    
