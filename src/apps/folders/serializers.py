from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.folders.models import Folder as FolderModel


class FolderSerializer(serializers.ModelSerializer):
    files = serializers.ListField(
        write_only=True, required=False, child=serializers.IntegerField(min_value=0)
    )

    def create(self, validated_data):
        title = validated_data.get("title")
        user = self.context.get("request", None).user

        new_folder = FolderModel.objects.create(title=title, user=user)
        return new_folder

    def update(self, instance, validated_data):
        files_id = validated_data.get("files")
        for i in files_id:
            instance.files.add(i)
        instance.save()
        return instance

    class Meta:
        model = FolderModel
        fields = ("id", "title", "files")


class FolserFilesSerializer(serializers.ModelSerializer):
    ACTION_CHOICES = (("add", "add"), ("remove", "remove"))

    files_id = serializers.ListField(
        write_only=True, child=serializers.IntegerField(min_value=0)
    )

    action = serializers.ChoiceField(write_only=True, choices=ACTION_CHOICES)

    def update(self, instance, validated_data):
        files_id = validated_data.pop("files_id")
        action = validated_data.pop("action")

        for file_id in files_id:
            if action == "add":
                instance.files.add(file_id)
            elif action == "remove":
                instance.files.remove(file_id)
            else:
                raise ValidationError("The action kwarg must be 'add' or 'remove'.")
            instance.save()

        return instance

    class Meta:
        model = FolderModel
        fields = ("files_id", "action")
