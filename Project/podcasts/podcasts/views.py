from django.shortcuts import render, get_object_or_404, redirect
from .models import Podcast
from django.contrib.auth.decorators import login_required
from .forms import PodcastUploadForm
import re

# Podcast list view with Search
def podcast_list(request):
    query = request.GET.get('q')
    if query:
        podcasts = Podcast.objects.filter(title__icontains=query)
    else:
        podcasts = Podcast.objects.all()
    return render(request, 'podcasts/podcast_list.html', {'podcasts': podcasts})

# Podcast Detail View
def podcast_detail(request, id):
    podcast = get_object_or_404(Podcast, id=id)
    return render(request, 'podcasts/podcast_detail.html', {'podcasts': podcast})

# Podcast Upload View
@login_required
def upload_podcast(request):
    if request.method == "POST":
        form = PodcastUploadForm(request.POST, request.FILES)
        if form.is_valid():
            podcast = form.save(commit=False)
            podcast.uploaded_by = request.user
            podcast.save()
            return redirect('podcasts:podcast_list')  # Changed from list_podcasts to podcast_list
    else:
        form = PodcastUploadForm()
    return render(request, "podcasts/upload_podcast.html", {"form": form})


# Podcast Streaming View
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
import os
import re

def stream_podcast(request, id):
    podcast = get_object_or_404(Podcast, id=id)
    
    # For template rendering (player UI)
    if request.method == 'GET' and not request.META.get('HTTP_RANGE'):
        return render(request, 'podcasts/stream.html', {'podcast': podcast})
    
    # Handle actual video streaming with range requests
    path = podcast.video.path
    file_size = os.path.getsize(path)
    
    # Get range header
    range_header = request.META.get('HTTP_RANGE', '').strip()
    range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
    
    if range_match:
        start = int(range_match.group(1))
        end = int(range_match.group(2)) if range_match.group(2) else file_size - 1
    else:
        start = 0
        end = file_size - 1
        
    # Calculate chunk size
    chunk_size = end - start + 1
    
    # Create response
    response = StreamingHttpResponse(
        file_iterator(path, start, chunk_size),
        status=206,
        content_type='video/mp4'  # Adjust based on your file type
    )
    
    # Add content range header
    response['Content-Range'] = f'bytes {start}-{end}/{file_size}'
    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = chunk_size
    
    return response

def file_iterator(path, start, chunk_size):
    """Function to yield file chunks"""
    with open(path, 'rb') as f:
        f.seek(start)
        remaining = chunk_size
        while remaining > 0:
            data = f.read(min(remaining, 8192))
            if not data:
                break
            remaining -= len(data)
            yield data
            
            
            
# Welcome Page
def welcome(request):
    return render(request, "welcome.html")

