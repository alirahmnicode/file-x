from rest_framework import serializers
from apps.multimedia.models import File as FileModel


class FileSerializer(serializers.ModelSerializer):
    file_size = serializers.SerializerMethodField("get_file_size")

    def get_file_size(self, obj):
        size = obj.file_size
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
        user = self.context.get("request").user
        files = validated_data.get("files")
        files_list = []

        for file in files:
            new_file = FileModel(file=file, user=user)
            new_file.file_format = new_file.get_file_format()
            new_file.file_name = new_file.get_file_name()
            new_file.file_size = new_file.get_file_size()
            files_list.append(new_file)

        created_file = FileModel.objects.bulk_create(files_list)
        return created_file
