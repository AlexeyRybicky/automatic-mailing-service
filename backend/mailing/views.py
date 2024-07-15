"""В модуле содержаться классы представлений для приложения `mailing`"""

from rest_framework import viewsets

from mailing.models import Client, Mailing, Message, Tag
from mailing.serializers import ClientSerializer, MailingSerializer, MessageSerializer, TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    Представляет собой стандартный набор CRUD
    для взаимодействия с сущностью `Tag`
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    Представляет собой стандартный набор CRUD
    для взаимодействия с сущностью `Client`
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    """
    Представляет собой стандартный набор CRUD
    для взаимодействия с сущностью `Mailing`
    """

    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    Представляет собой стандартный набор CRUD
    для взаимодействия с сущностью `Message`
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
