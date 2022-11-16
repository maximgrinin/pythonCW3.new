import os

# Определяем глобальные настройки
POST_PATH = os.path.join("data", "data.json")
COMMENT_PATH = os.path.join("data", "comments.json")
BM_PATH = os.path.join("data", "bookmarks.json")
LOG_DIR = "log"
LOG_PATH = os.path.join(LOG_DIR, "main_log.log")
UPLOAD_FOLDER = os.path.join("uploads", "images")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
LOGGER_FORMAT = "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s"
LOGGER_FORMAT_DATE = "%m.%d.%Y %H:%M:%S"
