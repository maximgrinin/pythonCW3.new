import pytest
import run


# создаем фикстуру для тестирования всех вьюшек (main, api, bookmarks)
@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()

@pytest.fixture()
def cat():
    return "meow"
