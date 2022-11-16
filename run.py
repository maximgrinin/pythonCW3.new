from flask import Flask, send_from_directory
from config_logger import logger_configure
from app.main.views import main_blueprint
from app.api.views import api_blueprint
from exceptions.exceptions import DataSourceError

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint, url_prefix="/api")

app.config['JSON_AS_ASCII'] = False
#app.json.ensure_ascii = False

logger_configure()


# Вьюшка для загрузки данных пользователя
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


# Вьюшка для обработки 404 ошибки
@app.errorhandler(404)
def page_error_404(error):
    return f"Такой страницы нет: {error}", 404


# Вьюшка для обработки 500 ошибки
@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере произошла ошибка: {error}", 500


# Вьюшка для обработки ошибки получения данных
@app.errorhandler(DataSourceError)
def page_error_data_source_error(error):
    return f"Ошибка с получением данных: {error}", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
