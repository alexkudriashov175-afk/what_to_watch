# opinions_app/__init__.py
from flask import Flask
from flask_migrate import Migrate

from settings import Config

from .models import db


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# --- Импорты в конце файла ---
# views/error_handlers/cli_commands зависят от db и app,
# созданных выше. Импортируем их после инициализации,
# чтобы избежать циклических зависимостей.
from . import views                                            # noqa: E402,F401
from .cli_commands import load_opinions_command                # noqa: E402
from .error_handlers import internal_error, page_not_found     # noqa: E402


# Регистрация view-функций
app.add_url_rule('/', view_func=views.index_view)
app.add_url_rule(
    '/add',
    view_func=views.add_opinion_view,
    methods=['GET', 'POST'],
)
app.add_url_rule(
    '/opinion/<int:id>',
    view_func=views.opinion_view,
)

# Регистрация обработчиков ошибок
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, internal_error)

# Регистрация CLI-команд
app.cli.add_command(load_opinions_command)