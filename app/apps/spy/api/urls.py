from django.urls import path

from .views import (
    CatListCreateAPIView,
    CatRetrieveUpdateDestroyAPIView,
    MissionListCreateAPIView,
    MissionRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("cats/", CatListCreateAPIView.as_view()),
    path("cats/<int:pk>/", CatRetrieveUpdateDestroyAPIView.as_view()),
    path("missions/", MissionListCreateAPIView.as_view()),
    path("missions/<int:pk>/", MissionRetrieveUpdateDestroyAPIView.as_view()),
]
