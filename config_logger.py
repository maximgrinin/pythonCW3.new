from config import LOG_DIR, LOG_PATH, LOGGER_FORMAT, LOGGER_FORMAT_DATE
import logging
import os


def logger_configure():
    # Позаботимся чтобы была папка с логами
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Создаем регистратор с именем 'api_logger'
    api_logger = logging.getLogger("api_logger")
    api_logger.setLevel(logging.DEBUG)
    # Создаем файловый обработчик, который регистрирует отладочные сообщения
    file_handler = logging.FileHandler(LOG_PATH)
    file_handler.setLevel(logging.DEBUG)
    # Создаем консольный обработчик с более высоким уровнем журнала
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    # Создаем форматтер и добавляем его в обработчики
    formatter = logging.Formatter(LOGGER_FORMAT, LOGGER_FORMAT_DATE)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # Добавляем настроенные обработчики в логгер
    api_logger.addHandler(file_handler)
    api_logger.addHandler(console_handler)
