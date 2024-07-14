"""В модуле содержаться тесты для моделей базы данных приложения `mailing`"""

from django.db import transaction, DataError, IntegrityError
from django.test import TestCase
from mailing.models import Client


class MailingCreateTests(TestCase):

    def setUp(self):
        self.assertEqual(Client.objects.count(), 0)

    def test_create_clint(self):
        """Тест для проверки создания объекта `Client`"""

        fake_phone_number = '71234567890'
        fake_mobile_operator_code = '909'
        fake_tag = 'новый'

        client = Client.objects.create(
            phone_number=fake_phone_number,
            mobile_operator_code=fake_mobile_operator_code,
            tag=fake_tag
        )
        self.assertEqual(Client.objects.count(), 1)

        client_db = Client.objects.get(pk=client.pk)
        self.assertEqual(client_db.phone_number, fake_phone_number)

    def test_too_big_phone_number(self):
        """Тест для проверки длины номера телефона"""

        with self.assertRaises(DataError):
            with transaction.atomic():
                Client.objects.create(phone_number="7" * 12)

        self.assertEqual(Client.objects.count(), 0)

    def test_not_nullable_phone_number(self):
        """Тест для првоерки пустого номера телефона"""

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Client.objects.create(
                    phone_number=None,
                    mobile_operator_code=None,
                    tag=None
                )

        self.assertEqual(Client.objects.count(), 0)

    def test_too_big_mobile_operator_code(self):
        """Тест для проверки длины мобильного оператора"""

        with self.assertRaises(DataError):
            with transaction.atomic():
                Client.objects.create(
                    phone_number="79005754563",
                    mobile_operator_code="1" * 4,
                )

        self.assertEqual(Client.objects.count(), 0)

    def test_nullable_mobile_operator_code(self):
        """
        Тест для проверки создания объекта с пустым полем код оператора
        """

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Client.objects.create(
                    phone_number="79005754563",
                    mobile_operator_code=None,
                    tag=None,
                )

        self.assertEqual(Client.objects.count(), 0)

    def test_not_nullable_mobile_operator_code(self):
        """
        Тест для проверки создания объекта не с пустым полем тег
        """

        Client.objects.create(
            phone_number="79005754563",
            mobile_operator_code='123',
            tag=None,
        )

        self.assertEqual(Client.objects.count(), 1)

    def test_too_big_tag(self):
        """Тест для проверки длины тега"""

        with self.assertRaises(DataError):
            with transaction.atomic():
                Client.objects.create(
                    phone_number="79005754563",
                    mobile_operator_code="123",
                    tag='новый' * 5
                )

        self.assertEqual(Client.objects.count(), 0)




