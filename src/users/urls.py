from django.urls import path

from .views import LoginAPIView, Signup, CurrentUser


app_name = "user"

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('signup/', Signup.as_view()),
    path('me/', CurrentUser.as_view()),
]