from django.contrib import admin
from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import Login, Register

app_name = "users"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", Login.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("register/", Register.as_view()),
    path("my-transactions/", GetTransactions.as_view()),
    path("transfer/", Transfer.as_view()),
]

