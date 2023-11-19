from rest_framework.routers import SimpleRouter

from apps.multimedia.views import FileViewSet


router = SimpleRouter()

router.register("", FileViewSet, basename="files")
urlpatterns = [] + router.urls