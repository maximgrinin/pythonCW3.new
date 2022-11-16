import pytest


class TestApi:
    post_keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    def test_api_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код при обращении к списку постов"""
        response = test_client.get('/api/', follow_redirects=True)
        assert response.status_code == 200, "Статус-код для корня API неверный"

    def test_api_posts_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код при обращении к списку постов"""
        response = test_client.get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус-код для API всех постов неверный"

    def test_api_comments_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код при обращении к списку комментариев """
        response = test_client.get('/api/comments', follow_redirects=True)
        assert response.status_code == 200, "Статус-код для API списка комментариев неверный"

    def test_api_post_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код при обращении к одному посту """
        response = test_client.get('/api/posts/1', follow_redirects=True)
        assert response.status_code == 200, "Статус-код для API одного поста неверный"

    def test_api_post_status_404(self, test_client):
        """ Проверяем, получается ли нужный статус-код при обращении к несуществующему посту """
        response = test_client.get('/api/posts/0', follow_redirects=True)
        assert response.status_code == 404, "Статус-код для API несуществующего поста неверный"

    @pytest.mark.parametrize("pk", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_api_post_keys(self, test_client, pk):
        """ Проверяем, верный ли набор полей при обращении к единичному посту """
        response = test_client.get(f'/api/posts/{pk}', follow_redirects=True)
        post = response.get_json()
        post_keys = set(post.keys())
        assert post_keys == self.post_keys_should_be , "При запросе одного поста неверный набор полей"

    def test_api_all_posts_keys(self, test_client):
        """ Проверяем, верный ли набор полей при обращении к списку постов """
        response = test_client.get('/api/posts', follow_redirects=True)
        posts_list = response.get_json()
        for post in posts_list:
            assert post.keys() == self.post_keys_should_be , "При запросе списка постов неверный набор полей"

    def test_meow(self, cat):
        assert cat == "meow"
