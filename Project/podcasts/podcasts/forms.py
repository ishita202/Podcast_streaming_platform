from django import forms
from .models import Podcast

class PodcastUploadForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ['title', 'description', 'video']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter podcast title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter podcast description'}),
            'video': forms.FileInput(attrs={'class': 'form-control', 'accept': 'video/mp4,video/x-m4v,video/*'})
        }