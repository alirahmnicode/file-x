from rest_framework import serializers
from apps.multimedia.models import Folder, File
from django.core.files.base import ContentFile


class FolderSerializers(serializers.ModelSerializer):

    def create(self, validated_data):
        title = validated_data.get("title")
        user = self.context.get("request", None).user

        new_folder = Folder.objects.create(title=title, user=user)
        # file_instance = File(user=user, file=files)
        # file_instance.save()
        # new_folder.files.add(file_instance)
        # new_folder.save()
        # if files:
        #     for file in files:
        #         print(file)
        #         file_instance = File(user=user, file=ContentFile(file))
        #         file_instance.save()
        #         new_folder.files.add(file_instance)
        #     new_folder.save()

        return new_folder

    class Meta:
        model = Folder
        fields = ("id", "title")