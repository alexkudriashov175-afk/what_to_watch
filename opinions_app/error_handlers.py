"""Обработчики ошибок приложения «Что посмотреть?»."""

from flask import render_template

from .models import db


def page_not_found(error):
    """Вернуть страницу 404."""
    return render_template('404.html'), 404


def internal_error(error):
    """Вернуть страницу 500 и откатить сессию БД."""
    db.session.rollback()
    return render_template('500.html'), 500
