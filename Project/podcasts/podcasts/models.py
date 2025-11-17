from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to="podcasts/videos/")
    thumbnail = models.ImageField(upload_to="podcasts/thumbnails/", null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0)  # Add this to track views
    duration = models.CharField(max_length=10, null=True, blank=True)  # For storing video duration (HH:MM:SS)
    
    def __str__(self):
        return self.title