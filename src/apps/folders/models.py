from django.db import models
from django.conf import settings

from libs.db.models import AuditableModel



class Folder(AuditableModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="folders"
    )
    title = models.CharField(max_length=256)
    files = models.ManyToManyField("multimedia.File", related_name="files", blank=True)

    
    def __str__(self):
        return f"{self.title} - {self.user.username}"