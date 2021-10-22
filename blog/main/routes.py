from flask import Blueprint, render_template, request
from blog import db
from blog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
def paginate_posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.paginate(page=page, per_page=20)
    if not posts.total >= 100:
        for i in range(1, 101):
            post = Post(title=f'New post', content=f'Я создан автоматически, мой номер {i}')
            db.session.add(post)
        db.session.commit()

    return render_template('index.html', posts=posts)
