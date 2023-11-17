from django.db import models
from django.conf import settings

from libs.db.models import AuditableModel


class File(AuditableModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to="documents/%Y/%m/%d")


class Folder(AuditableModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="folders"
    )
    title = models.CharField(max_length=256)
    files = models.ManyToManyField(File, related_name="files", blank=True)
