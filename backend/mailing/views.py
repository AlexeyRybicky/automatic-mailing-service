"""В модуле содержаться классы представлений для приложения `mailing`"""

import datetime
from functools import reduce
from operator import and_

from django.db.models import Q
from django.shortcuts import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from mailing.models import Client, Mailing, Message, Tag
from mailing.parser import Parser
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
