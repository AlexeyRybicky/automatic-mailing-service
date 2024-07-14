"""В моделу хранятся роутеры проекта"""

from rest_framework.routers import SimpleRouter

from mailing.views import ClientViewSet, MailingViewSet, MessageViewSet, TagViewSet

router = SimpleRouter()
router.register(r'client', ClientViewSet, basename='client')
router.register(r'mailing', MailingViewSet, basename='mailing')
router.register(r'message', MessageViewSet, basename='message')
router.register(r'tag', TagViewSet, basename='tag')
