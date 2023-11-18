from rest_framework.routers import SimpleRouter

from apps.multimedia.views import FolderViewSet


router = SimpleRouter()

router.register("", FolderViewSet, basename="folders")
urlpatterns = [] + router.urls