"""В модуле содержаться модели базы данных приложения `mailing`"""

from django.db import models


class Client(models.Model):
    """Модель `Client` содержит информацию о клиентах"""

    objects: models.Manager

    phone_number = models.CharField(
        max_length=11,
        unique=True,
        null=False,
        verbose_name='Номер телефона',
        help_text='номер телефона клиента в формате '
                  '7XXXXXXXXXX (X - цифра от 0 до 9)'
    )
    mobile_operator_code = models.IntegerField(
        null=False,
        verbose_name='Код оператора',
        help_text='код мобильного оператора'
    )
    tag = models.ManyToManyField(
        'mailing.Tag',
        related_name='tags',
        verbose_name='Тег',
        help_text=' Тег (произвольная метка)'
    )

    # pylint: disable=missing-docstring
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Tag(models.Model):
    objects: models.Manager

    name = models.CharField(
        unique=True,
        max_length=10,
        verbose_name='Тег',
        help_text=' Тег (произвольная метка)'
    )


class Mailing(models.Model):
    """Модель `Mailing` содержит информацию о рассылках"""

    objects: models.Manager

    start_time = models.DateTimeField(
        verbose_name='Начало рассылки',
        help_text='Дата и время запуска рассылки'
    )
    end_time = models.DateTimeField(
        verbose_name='Окончание рассылки',
        help_text='Дата и время окончания рассылки.'
                  'По окончании времени сообщения отправляться не должны'
    )
    message_text = models.CharField(
        max_length=200,
        verbose_name='Текст сообщения',
        help_text='Текст сообщения для доставки клиенту'
    )
    mobile_operator_filter = models.JSONField()
    tag_filter = models.ManyToManyField(
        'mailing.Tag',
        max_length=50,
    )

    # pylint: disable=missing-docstring
    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    """Модель `Message` содержит информацию об отправленных сообщениях"""

    objects: models.Manager

    creation_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания/отправки',
        help_text='дата и время создания (отправки) сообщения'
    )
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        verbose_name='ID расслыки',
        help_text='id рассылки, в рамках которой было отправлено сообщение'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='ID клиента',
        help_text=' id клиента, которому отправили'
    )

    # pylint: disable=missing-docstring
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
