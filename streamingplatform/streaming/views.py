from django.shortcuts import render
from .models import Video
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page"""
    videos = Video.objects.all()

    context = {
        'videos': videos,
    }

    return render(request, 'index.html', context)


class VideoDetailView(generic.DetailView):
    model = Video
