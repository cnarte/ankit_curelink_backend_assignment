from django.urls import path

from . import views

urlpatterns = [
   path("adduser/",views.ingest ),
   path("schedule_content/", views.schedule_content)
]
