from rest_framework.routers import SimpleRouter
from django.urls import path

from apps.folders.views import FolderViewSet, EditFolderFilesView


router = SimpleRouter()

router.register("", FolderViewSet, basename="folders")
urlpatterns = [path("<int:pk>/edit/files/", EditFolderFilesView.as_view())] + router.urls