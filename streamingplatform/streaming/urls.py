from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video/<int:pk>', views.VideoDetailView.as_view(), name='video-view')
]
