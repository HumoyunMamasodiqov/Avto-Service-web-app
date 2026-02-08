from django.urls import path
from .views import register, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path("logout/", user_logout, name="logout"),
]

