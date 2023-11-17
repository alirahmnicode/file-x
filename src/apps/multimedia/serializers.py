from rest_framework import serializers
from apps.multimedia.models import Folder


class FolderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"