from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "CoreApp"   


urlpatterns = [
    path("", views.home, name="home"),
    path("uploadToDB",views.uploadFileToDB, name = "upload_file_to_db")
    
    ]