from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from apps.folders.models import Folder as FolderModel
from apps.folders.serializers import FolderSerializer, FolserFilesSerializer


class FolderViewSet(ModelViewSet):
    queryset = FolderModel.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class EditFolderFilesView(UpdateAPIView):
    queryset = FolderModel.objects.all()
    http_method_names = ["patch"]
    serializer_class = FolserFilesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)