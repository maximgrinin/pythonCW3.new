from json import load as json_load, JSONDecodeError
from app.main.dao.post import Post
from exceptions.exceptions import DataSourceError


# Класс с функциями доступа к данным для Постов
class PostDAO:
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

    def load_posts(self):
        """ Преобразует данные в список элементов класса """
        posts_data = self.load_data()
        posts_list = [Post(**post_data) for post_data in posts_data]

        return posts_list

    def get_all(self):
        """ Возвращает список постов со всеми данными """
        posts = self.load_posts()

        return posts

    def get_by_pk(self, pk):
        """ Возвращает один пост по его идентификатору"""
        if type(pk) != int:
            raise TypeError("Идентификатор поста должен быть целым числом")
        posts = self.load_posts()
        for post in posts:
            if pk == post.pk:
                return post

    def search_for_posts(self, query):
        """
        Возвращает список постов по ключевому слову
        """
        query = str(query).strip().lower()
        posts = self.load_posts()
        posts_list = [post for post in posts if query in post.content.strip().lower()]

        return posts_list

    def get_by_user(self, user_name):
        """
        Возвращает посты определенного пользователя
        """
        user_name = str(user_name).strip().lower()
        posts = self.load_posts()
        posts_list = [post for post in posts if user_name == post.poster_name.strip().lower()]

        return posts_list
