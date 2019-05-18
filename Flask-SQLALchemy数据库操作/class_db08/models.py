# encoding:utf-8

from exts import db

# 循环引用

# app = Flask(__name__)
# db = SQLAlchemy(app)

class Article(db.Model):
    __tablename = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)







