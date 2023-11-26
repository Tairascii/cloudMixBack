from django.urls import path, re_path

from .views import ChatsViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'chats', ChatsViewSet, basename='chats')

urlpatterns = router.urls
