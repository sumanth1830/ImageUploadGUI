from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("imageupload", views.simple_upload),
    path("posefinder", views.image_pose_finder)
]