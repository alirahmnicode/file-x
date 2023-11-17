from django.urls import path

from .views import LoginAPIView, Signup


urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('signup/', Signup.as_view()),
]