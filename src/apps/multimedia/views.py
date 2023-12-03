from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from apps.multimedia.models import File
from apps.multimedia.serializers import UploadMultipleFileSerializer, FileSerializer


class CustomFileModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    pass


class FileViewSet(CustomFileModelViewSet):
    queryset = File.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "create":
            return UploadMultipleFileSerializer
        else:
            return FileSerializer


class RecentFilesView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user_files = queryset.filter(user=self.request.user)
        return user_files[:10]        


