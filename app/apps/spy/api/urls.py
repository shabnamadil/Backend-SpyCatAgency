from django.urls import path

from .views import (
    CatListCreateAPIView,
    CatRetrieveUpdateDestroyAPIView,
    MissionListCreateAPIView,
    MissionRetrieveUpdateDestroyAPIView,
    TargetRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("cats/", CatListCreateAPIView.as_view()),
    path("cats/<int:pk>/", CatRetrieveUpdateDestroyAPIView.as_view()),
    path("missions/", MissionListCreateAPIView.as_view()),
    path("missions/<int:pk>/", MissionRetrieveUpdateDestroyAPIView.as_view()),
    path("targets/<int:pk>/", TargetRetrieveUpdateDestroyAPIView.as_view()),
]
