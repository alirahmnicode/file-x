from rest_framework import serializers
from apps.multimedia.models import File as FileModel


class FileSerializer(serializers.ModelSerializer):
    file_format = serializers.SerializerMethodField("get_file_format")
    file_name = serializers.SerializerMethodField("get_file_name")
    file_size = serializers.SerializerMethodField("get_file_size")

    def get_file_format(self, obj):
        return obj.file.name.split(".")[-1]

    def get_file_name(self, obj):
        return obj.file.name.split("/")[-1]

    def get_file_size(self, obj):
        size = obj.file.size
        if size < 1_000_000:
            return f"{size / 1_000}kb"
        else:
            return f"{size / 1_000_000}mb"

    class Meta:
        model = FileModel
        fields = ("id", "file", "file_format", "file_name", "file_size")


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
