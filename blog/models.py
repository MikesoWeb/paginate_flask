from blog import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(60), nullable=False)

    def __repr__(self):
        return f'Post model( {self.id}, {self.title}, {self.content})'
