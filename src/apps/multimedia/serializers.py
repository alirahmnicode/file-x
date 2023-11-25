from rest_framework import serializers
from apps.multimedia.models import File as FileModel


class FileSerializer(serializers.ModelSerializer):
    file_format = serializers.SerializerMethodField("get_file_format")

    def get_file_format(self, obj):
        return obj.file.name.split(".")[-1]

    class Meta:
        model = FileModel
        fields = ("id", "file", "file_format")


class UploadMultipleFileSerializer(serializers.Serializer):
    files = serializers.ListField(
        write_only=True,
        child=serializers.FileField(allow_empty_file=False, use_url=False),
    )

    def create(self, validated_data):
        files = validated_data.get("files")
        user = self.context.get("request").user
        files_list = []

        files_list = [FileModel(file=file, user=user) for file in files]

        created_file = FileModel.objects.bulk_create(files_list)
        return created_file
