"""Настройки приложения «Что посмотреть?»."""

import os


class Config(object):
    """Конфигурация Flask-приложения."""

    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', default='sqlite:///db.sqlite3'
    )
    SECRET_KEY = os.getenv('SECRET_KEY', default='MY_SECRET_KEY')
