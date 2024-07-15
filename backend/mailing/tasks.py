"""В модуле содержиться задача celery для автоматической отправки рассылки"""

import datetime
from functools import reduce
from operator import and_

from celery import shared_task

from mailing.models import Mailing, Client, Message
from mailing.parser import Parser


@shared_task
def send_message():
    """
    Celery задача периодически проверяет таблицу рассылок (Mailing)
    на наличие активных рассылок, фильтрует клиентов по заданным условиям и отправляет им сообщения.
    """

    current_time = datetime.datetime.now(datetime.timezone.utc)
    mailings = Mailing.objects.filter(start_time__lte=current_time, end_time__gte=current_time)

    for mailing in mailings:
        filter_conditions = []
        if mailing.mobile_operator_filter:
            filter_conditions.append({"mobile_operator_code__lte": mailing.mobile_operator_filter})
        if mailing.tag_filter.all():
            filter_conditions.append({"tag__in": [tag.id for tag in mailing.tag_filter.all()]})

        if filter_conditions:
            clients = Client.objects.filter(reduce(and_, Parser.parse(filter_conditions)))
        else:
            clients = Client.objects.all()

        for client in clients:
            message = Message(client=client, mailing=mailing)
            message.save()
            print(f'Сообщение {mailing.message_text} отправлено клиенту {client.phone_number}')
