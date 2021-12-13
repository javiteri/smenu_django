from django.conf.urls import url
from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter
from users.api.views import UserApipViewSet, UserView

router_user = DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=UserApipViewSet
)

urlpatterns = [
    path('auth/me', UserView.as_view())
]
