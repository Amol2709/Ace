from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "CoreApp"   


urlpatterns = [
    path("", views.home, name="home"),
    path("validate_file",views.validateFileExtension, name = "validate_file"),
    path("upload_file_to_db",views.uploadFileToDB, name = "upload_file_to_db"),
    path("view_info/",views.viewInfo, name = "view_info")
    
    ]