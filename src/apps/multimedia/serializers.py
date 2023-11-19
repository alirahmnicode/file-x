from rest_framework import serializers
from apps.multimedia.models import File



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ("file",)