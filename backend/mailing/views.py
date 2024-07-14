"""В модуле содержаться классы представлений для приложения `mailing`"""


from rest_framework import viewsets

from mailing.models import Client, Mailing, Message, Tag
from mailing.serializers import ClientSerializer, MailingSerializer, MessageSerializer, TagSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
