"""
TODO:
# Задание со звездочкой
### Шаг 1 – Реализуйте переход по тегам
Вернитесь к представлению, которое выводит пост. В тексте поста отыщите слова, выберите такие, которые начинаются с `#` и превратите их ссылки по принципу `#food` >>> `<a href="/tag/food">#food</a>`
Создайте представление для `/tag/<tagname>.` В списке постов отыщите такие, которые содержат тег, начинающийся с решетки. Выведите их в соответствующем шаблоне
### Шаг 2 – добавьте посты в закладки.
Создайте представление с добавлением в закладки по маршруту `bookmarks/add/postid`.
Храните закладки в файле `bookmarks.json`.
После добавления переадресуйте на главную страницу. (`/`)
Для переадресации (редиректа) используйте
```python
#  Для переадресации (редиректа) используйте
return redirect("адрес", code = 302)
```
Создайте представление с удалением из закладок по маршруту `bookmarks/remove/postid`.
После удаления закладки переадресовывайте на главную страницу (`/`)
### Шаг 3 – выведите закладки
Добавьте представление `/bookmarks` для просмотра всех закладок — покажите там все посты, которые добавлены в закладки. Данные возьмите из `bookmarks.json`.
### Подсказка:
Чтобы вывести в шаблоне строку, которая содержит HTML-теги, используйте `{{ content|safe }}` – это специальный синтаксис, который разрешает выводить теги "живые" теги, а не их текстовое представление.
"""
from flask import Blueprint, request, render_template, abort
from app.main.dao.post import Post
from app.main.dao.post_dao import PostDAO
from app.main.dao.comment import Comment
from app.main.dao.comment_dao import CommentDAO
from config import POST_PATH, COMMENT_PATH


# Создаем блупринт
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

# Создаем DAO постов и комментариев
post_dao = PostDAO(POST_PATH)
comment_dao = CommentDAO(COMMENT_PATH)


# Вьюшка для списка постов при обращении к корню
@main_blueprint.route("/")
def index_page():
    posts_list = post_dao.get_all()
    return render_template('index.html', posts=posts_list)


# Вьюшка для поста при обращении по его pk
@main_blueprint.route("/post/<int:pk>")
def page_id(pk):
    post: Post | None = post_dao.get_by_pk(pk)
    comments: list[Comment] = comment_dao.get_by_post_id(pk, post)

    if post is None:
        abort(404, "Такого поста не существует")

    return render_template('post.html', post=post, comments=comments)


# Вьюшка для поиска поста по описанию
@main_blueprint.route('/search')
def search_page():
    # Обрабатываем параметры, отбираем посты, где содержится фраза поиска
    tag: str = request.args.get("s", "")
    post_list = post_dao.search_for_posts(tag)

    return render_template('search.html', tag=tag, posts=post_list)


# Вьюшка для всех постов по пользователю
@main_blueprint.route('/users/<username>')
def user_page(username):
    # Обрабатываем параметры, отбираем посты, где содержится фраза поиска
    post_list = post_dao.get_by_user(username)

    if not post_list:
        abort(404, "Такого пользователя не существует")

    return render_template('user-feed.html', username=username, posts=post_list)
