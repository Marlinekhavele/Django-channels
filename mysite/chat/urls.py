from django.urls import path

from . import views
from .views import index, room

app_name = "chat"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
]
