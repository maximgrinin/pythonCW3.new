from json import load as json_load, JSONDecodeError
from app.main.dao.comment import Comment
from app.main.dao.post import Post
from exceptions.exceptions import DataSourceError


# Класс с функциями доступа к данным для Комментариев
class CommentDAO:
    def __init__(self, path):
        """ При создании экземпляра DAO указываем путь к файлу с данными """
        self.path = path

    def load_data(self):
        """ Загружает данные из файла и возвращает обычный list """
        try:
            with open(self.path, 'r', encoding="utf-8") as file:
                json = json_load(file)
        except FileNotFoundError as e:
            # Будет выполнено, если файл не найден
            raise DataSourceError(f"Не удается получить данные из файла: {e}")
        except JSONDecodeError:
            # Будет выполнено, если файл найден, но не превращается из JSON
            raise DataSourceError(f"Не удается разобрать полученные из файла данные")

        return json

    def load_comments(self):
        """ Преобразует данные в список элементов класса """
        comments_data = self.load_data()
        comments_list = [Comment(**comment_data) for comment_data in comments_data]

        return comments_list

    def get_all(self):
        """ Возвращает список комментариев со всеми данными """
        comments = self.load_comments()

        return comments

    # Функция возвращает комментарии определенного поста
    # Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов
    def get_by_post_id(self, post_id: int, post: Post) -> list[Comment]:
        """
        Возвращает комментарии определенного поста
        """
        if post is None:
            raise ValueError(f"Запрошены комментарии к несуществующему посту. post_id: {post_id}")

        comments: list[Comment] = self.get_all()
        comments_for_post: list[Comment] = [comment for comment in comments if comment.post_id == post.pk]

        return comments_for_post
