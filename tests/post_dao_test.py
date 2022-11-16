from app.main.dao.post_dao import PostDAO
from app.main.dao.post import Post
import pytest


def check_fields(post):
    # Задаем, какие ключи ожидаем получать у постов
    keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    for key in keys_should_be:
        assert hasattr(post, key), f"Нет поля {key}"


# Класс тестирования функций получения данных для поста
class TestPostDAO:
    # Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
    # Но пригодится только один раз, поэтому выносить в conftest не будем
    @pytest.fixture()
    def post_dao(self):
        post_dao_instance = PostDAO("data/data.json")
        return post_dao_instance

    def test_get_all(self, post_dao):
        """ Тестируем получение всех постов """
        posts = post_dao.get_all()
        post = posts[0]
        assert type(posts) == list, "При получении всех постов возвращается не список"
        assert len(posts) > 0, "При получении всех постов возвращается пустой список"
        assert type(post) == Post, "При получении всех постов в элементе не Post"

    def test_get_all_keys(self, post_dao):
        """ Тестируем набор полей при получении всех постов """
        posts = post_dao.get_all()
        post = posts[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        """ Проверяем все ли pk постов на месте при получении всех постов """
        posts = post_dao.get_all()
        correct_ids = {1, 2, 3, 4, 5, 6, 7, 8}
        ids = set([post.pk for post in posts])
        assert ids == correct_ids, "При получеии всех постов не совпадают полученные pk"

    def test_get_by_id(self, post_dao):
        """ Проверяем, верный ли пост возвращается при запросе одного """
        post = post_dao.get_by_pk(1)
        assert type(post) == Post, "При запросе поста, возвращается не Post"
        check_fields(post)

        post = post_dao.get_by_pk(999)
        assert post is None, "Не None для несуществующего поста"

    @pytest.mark.parametrize("pk", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_get_by_id_correct_ids(self, post_dao, pk):
        """ Проверяем совпадение pk при запросе одного поста"""
        post = post_dao.get_by_pk(pk)
        assert post.pk == pk, f"Неверный pk для {post.pk}. Ожидался {pk}"

    def test_search_for_posts(self, post_dao):
        """ Проверяем поиск по постам """
        posts = post_dao.search_for_posts("Утро")
        post = posts[0]
        assert type(posts) == list, "При поиске постов возвращается не список"
        assert len(posts) > 0, "При поиске постов возвращается пустой список"
        assert type(post) == Post, "При поиске постов в элементе не Post"
        check_fields(post)

        posts = post_dao.search_for_posts("12345678900987654321")
        assert posts == [], "Ожидается [] для неудачного поиска"

    @pytest.mark.parametrize("query, expected_pks", [("Утро", {4, 8})])
    def test_search_for_posts_correct_ids(self, post_dao, query, expected_pks):
        """ Проверяем набор возвращаемых pk при поиске """
        posts = post_dao.search_for_posts(query)
        pks = set([post.pk for post in posts])
        assert pks == expected_pks, f"При поиске постов неверный набор pk"

    def test_get_by_user(self, post_dao):
        """ Проверяем получение постов по пользователю """
        posts = post_dao.get_by_user("LEO")
        post = posts[0]
        assert type(posts) == list, "При запросе постов пользователя возвращается не список"
        assert len(posts) > 0, "При запросе постов пользователя возвращается пустой список"
        assert type(post) == Post, "При запросе постов пользователя в элементе не Post"
        check_fields(post)

        posts = post_dao.get_by_user("skrzhecheck")
        assert posts == [], "Ожидается [] для несуществующего автора"

    @pytest.mark.parametrize("poster_name, expected_pks", [("leo", {1, 5})])
    def test_get_by_user_correct_ids(self, post_dao, poster_name, expected_pks):
        """ Проверяем набор возвращаемых pk при запросе по пользователю """
        posts = post_dao.get_by_user(poster_name)
        pks = set([post.pk for post in posts])
        assert pks == expected_pks, f"Неверный набор pk при поиске по пользователю"
