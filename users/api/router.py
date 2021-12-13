from django.db import router
from rest_framework.routers import DefaultRouter
from users.api.views import UserApipViewSet

router_user = DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=UserApipViewSet
)
