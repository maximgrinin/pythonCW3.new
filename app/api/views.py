from flask import Blueprint, jsonify, abort
from app.main.dao.post import Post
from app.main.dao.post_dao import PostDAO
from app.main.dao.comment import Comment
from app.main.dao.comment_dao import CommentDAO
from config import POST_PATH, COMMENT_PATH
import logging

# Создаем блупринт
api_blueprint = Blueprint('api_blueprint', __name__)

# Создаем DAO постов и комментариев
post_dao = PostDAO(POST_PATH)
comment_dao = CommentDAO(COMMENT_PATH)

# Создаем логгер
api_logger = logging.getLogger("api_logger")


# Вьюшка для АПИ при обращении к корню
@api_blueprint.route("/")
def get_posts_index_api():
    return "Доступные эндпоинты: api/posts и api/posts/, api/comments"


# Вьюшка для АПИ при обращении к полному списку постов
@api_blueprint.route("/posts")
def api_posts_all():
    # Логируем обращение к АПИ
    api_logger.info(f"Запрос /api/posts")

    # Получаем полный список постов и возвращаем его
    posts_list: list[Post] = post_dao.get_all()
    post_list_as_dict: list[dict] = [post.as_dict() for post in posts_list]

    return jsonify(post_list_as_dict), 200


# Вьюшка для АПИ при обращении к конкретному посту
@api_blueprint.route("/posts/<int:pk>")
def api_post_by_pk(pk):
    # Логируем обращение к АПИ
    api_logger.info(f"Запрос /api/posts/{pk}")

    # Получаем пост по его pk, если нет - возвращаем ошибку
    post: Post | None = post_dao.get_by_pk(pk)
    if post is None:
        api_logger.warning(f"Запрос к несуществующему посту /api/posts/{pk}")
        abort(404)

    return jsonify(post.as_dict()), 200


# Вьюшка для АПИ при обращении к полному списку комментариев
@api_blueprint.route("/comments")
def api_comments_all():
    # Логируем обращение к АПИ
    api_logger.info(f"Запрос /api/comments")

    # Получаем полный список комментариев и возвращаем его
    comments_list: list[Comment] = comment_dao.get_all()
    comments_list_as_dict: list[dict] = [comment.as_dict() for comment in comments_list]

    return jsonify(comments_list_as_dict), 200


# Вьюшка для обработки ошибки при обращении к несуществующей записи
# @api_blueprint.errorhandler(404)
def api_error_404(error):
    api_logger.error(f"Ошибка при обращении к API: {error}")
    return jsonify({"error": str(error)}), 404
