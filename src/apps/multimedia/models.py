from django.db import models
from django.conf import settings

from libs.db.models import AuditableModel


class File(AuditableModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="files"
    )

    file = models.FileField(upload_to="documents/%Y/%m/%d")
    file_name = models.CharField(max_length=1024, blank=True)
    file_format = models.CharField(max_length=5, blank=True)
    file_size = models.IntegerField(blank=True)
    

    def get_file_name(self):
        return self.file.name.split("/")[-1]
    
    def get_file_format(self):
        return self.file.name.split(".")[-1]
    
    def get_file_size(self):
        return self.file.size
    
    def save(self, *args, **kwargs) -> None:
        self.file_name = self.get_file_name()
        self.file_format = self.get_file_format()
        self.file_size = self.get_file_size()
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.file.name

    class Meta:
        ordering  = ("-created_at",)