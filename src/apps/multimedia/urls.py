from django.urls import path

from rest_framework.routers import SimpleRouter

from apps.multimedia.views import FileViewSet, RecentFilesView


router = SimpleRouter()

router.register("", FileViewSet, basename="files")
urlpatterns = [path("recent/", RecentFilesView.as_view()),] + router.urls
