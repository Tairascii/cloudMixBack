from django.urls import path, re_path

from .views import MessagesViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'messages', MessagesViewSet, basename='messages')

urlpatterns = [
    path(r'messages/<int:chat_id>/', MessagesViewSet.as_view({'get': 'list'})),
    path(r'messages/bot/', MessagesViewSet.as_view({'post': 'create_bot_reply'})),
]

urlpatterns += router.urls
