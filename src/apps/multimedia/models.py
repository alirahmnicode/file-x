from django.db import models
from django.conf import settings

from libs.db.models import AuditableModel


class File(AuditableModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="files"
    )
    file = models.FileField(upload_to="documents/%Y/%m/%d")
    
    def __str__(self) -> str:
        return self.file.name

    class Meta:
        ordering  = ("-created_at",)