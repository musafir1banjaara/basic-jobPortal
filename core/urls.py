from django.urls import path
from .views import home,create_job, delete_job, update_job

urlpatterns = [
    path("", home, name="home"),
    path("jobs/", create_job, name="create-job"),
    path("jobs/<int:id>/delete", delete_job, name="delete-job"),
    path("jobs/<int:id>/update", update_job, name="update-job"),
]


# <int:id> : create dynamic url path ie. we can give multiple integers here, everytime getting a new url path