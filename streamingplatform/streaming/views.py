from django.shortcuts import render
from .models import Video

# Create your views here.
def index(request):
    """View function for home page"""

    return render(request, 'index.html')