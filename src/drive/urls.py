from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings 

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
    SpectacularJSONAPIView,
)

from .views import index


doc_patterns = [
    path('api/schema/yaml/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/json/', SpectacularJSONAPIView.as_view(), name='json-schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/folder/', include(("apps.multimedia.urls", "apps.multimedia"), namespace="folders")),
    path("api/users/", include("users.urls")),
]

urlpatterns += doc_patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)