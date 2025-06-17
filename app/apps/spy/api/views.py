from django.core.exceptions import ValidationError
from .serializers  import CatListSerializer, CatPostSerializer, MissionPostSerializer, MissionListSerializer

from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from apps.spy.models import SpyCat, Mission
from rest_framework.response import Response
from rest_framework import status


class CatListCreateAPIView(ListCreateAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = CatListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = CatPostSerializer
        return super().get_serializer_class()
    

class CatRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SpyCat.objects.all()
    serializer_class = CatListSerializer

    def update(self, request, *args, **kwargs):
        # Only allow updating salary
        allowed_fields = ['salary']
        for field in request.data.keys():
            if field not in allowed_fields:
                return Response({'error': 'Only salary can be updated.'}, status=400)
        return super().update(request, *args, **kwargs)
    

class MissionListCreateAPIView(ListCreateAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionListSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            self.serializer_class = MissionPostSerializer
        return super().get_serializer_class()
    

class MissionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Mission.objects.all()
    serializer_class = MissionListSerializer

    def update(self, request, *args, **kwargs):
        # Only allow updating is_completed
        allowed_fields = ['is_completed']
        for field in request.data.keys():
            if field not in allowed_fields:
                return Response({'error': 'Only is_completed can be updated.'}, status=400)
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.cat:
            raise ValidationError("Cannot delete a mission that has a cat assigned.")
        return super().destroy(request, *args, **kwargs)