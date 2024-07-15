"""
В модуле содержиться алгоритм для парсинга сложных запросов
использует объекты Q для создания логических операций
"""

from functools import reduce
from operator import and_, or_

from django.db.models import Q


def _default_parser(key):
    """Функция по умолчанию для парсинга одиночных условий"""

    def _parser(value):
        return Q(**{f"{key}": value})
    return _parser


def _parser_and(value: list):
    """Функция объединяет условия с помощью логической операции AND"""

    return reduce(and_, Parser.parse(value))


def _parser_or(value: list):
    """Функция объединяет условия с помощью логической операции OR"""

    return reduce(or_, Parser.parse(value))


def _parser_not(value: list):
    """Функция отрицает условия с помощью логической операции NOT."""

    return ~reduce(and_, Parser.parse(value))


class Parser:
    """Класс чтения условий"""

    unary_manager = {
        "not": _parser_not,
    }
    binary_manager = {
        "and": _parser_and,
        "or": _parser_or,
    }

    @classmethod
    def parse(cls, conditions: dict | list[dict]):
        """Возвращает список объектов Q"""

        if isinstance(conditions, dict):
            conditions = [conditions]
        return [
            cls._parse_one_condition(*list(condition.items())[0])
            for condition in conditions
        ]

    @classmethod
    def _parse_one_condition(cls, key: str, val: dict | list[dict]):
        """Функция для чтения одного условия"""

        if cls.binary_manager.get(key):
            return cls.binary_manager[key](val)
        return cls.unary_manager.get(key, _default_parser(key))(val)
