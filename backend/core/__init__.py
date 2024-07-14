"""
Гарантирует, что приложение всегда будет импортировано при запуске Django
"""

from .celery import app as celery_app

__all__ = ('celery_app',)
