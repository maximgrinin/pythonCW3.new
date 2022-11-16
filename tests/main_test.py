class TestMain:

    def test_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код при обращении к списку постов"""
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус-код всех постов неверный"

    def test_post_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код при обращении к одному посту """
        response = test_client.get('/post/1', follow_redirects=True)
        assert response.status_code == 200, "Статус-код для одного поста неверный"

    def test_search_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код при обращении к странице поиска """
        response = test_client.get('/search?s=утро', follow_redirects=True)
        assert response.status_code == 200, "Статус-код поиска неверный"

    def test_user_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код при обращении к постам пользователя """
        response = test_client.get('/users/leo', follow_redirects=True)
        assert response.status_code == 200, "Статус-код пользователя неверный"
