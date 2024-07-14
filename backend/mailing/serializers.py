"""В модуле содержаться сериализаторы для приложения `mailing`"""

from django.apps import apps
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = apps.get_model('mailing', 'Client')
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model('mailing', 'Mailing')
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = apps.get_model('mailing', 'Message')
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('mailing', 'Tag')
        fields = '__all__'
