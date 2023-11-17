from django.urls import path

from .views import LoginAPIView, Signup, Test


urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('signup/', Signup.as_view()),
    path('test/', Test.as_view()),
]