from django.urls import path
from .views import home,create_job

urlpatterns = [
    path("", home, name="home"),
    path("add/", create_job, name="create_job"),
]
