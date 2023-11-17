from rest_framework.viewsets import ModelViewSet

from apps.multimedia.models import Folder
from apps.multimedia.serializers import FolderSerializers


class FolderViewSet(ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializers