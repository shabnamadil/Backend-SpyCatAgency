from apps.spy.models import Mission, SpyCat, Target
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from .serializers import (
    CatListSerializer,
    CatPostSerializer,
    MissionListSerializer,
    MissionPostSerializer,
    MissionUpdateSerializer,
    TargetListSerializer,
)


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
        allowed_fields = ["salary"]
        for field in request.data.keys():
            if field not in allowed_fields:
                return Response({"error": "Only salary can be updated."}, status=400)
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

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return MissionUpdateSerializer
        return super().get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.cat:
            return Response(
                {"error": "Cannot delete a mission that has a cat assigned."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)


class TargetRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Target.objects.all()
    serializer_class = TargetListSerializer

    def update(self, request, *args, **kwargs):
        # Only allow updating is_completed
        allowed_fields = ["is_completed", "notes"]
        target = self.get_object()
        for field in request.data.keys():
            if field not in allowed_fields:
                return Response(
                    {"error": "Only is_completed and notes can be updated."},
                    status=400,
                )
            if target.is_completed and target.mission.is_completed:
                return Response(
                    {
                        "error": "Notes cannot be updated if the target and mission is completed."
                    },
                    status=400,
                )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        target = self.get_object()
        if target.is_completed and target.mission.is_completed:
            return Response({"error": "Cannot delete a completed target."}, status=400)
        return super().destroy(request, *args, **kwargs)
