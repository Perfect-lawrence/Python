# encoding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


# user table
"""
create table users (
 id int primary key autoincrement,
 username varchar(100) not null
)
"""

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    # password = db.Column(db.String(100),nullable=False)


# article table
"""
create table article(
id int  primary key autoincretment,
title varchar(100) not null,
content text not null,
author_id int,
foreign key 'author_id' references 'users_id'

)
"""
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    # 反向引用
    author = db.relationship('User',backref=db.backref('articles'))

db.create_all()


@app.route('/')

def index():
    #  想要添加一篇文章必须依赖用户而存在，所以首先的话，先添加一个用户
    # 增加一条数据
    # user1 = User(username='zhangsan')
    # db.session.add(user1)
    # db.session.commit()
# 浏览器反问就插入一条数据  http://127.0.0.1:5000/  select * from user;

    #
    # article = Article(title='aaaa',content='bbb',author_id=1)
    # db.session.add(article)
    # db.session.commit()

    # 浏览器反问就插入一条数据  http://127.0.0.1:5000/  select * from article;


    #  要想找文章标题为aaa的作者
    #  查询数据库
    # article = Article.query.filter(Article.tittle == 'aaaa').first()
    # author_id = article.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print "username: %s" % user.username

    # article.author
    # author = User.query.filter(User.username == 'zhangsan')

    # article = Article(title='aaaa', content='bbb', author_id=1)
    # article.author = User.query.filter(User.id == 1).first()
    # db.session.add(article)
    # db.session.commit()

    # article = Article.query.filter(Article.title == 'aaaa').first()
    # print 'username: %s' % article.author.username

    # 我要找到zhangsan这个用户写过所有的文章
    # article = Article(title='yy',content='xyz',author_id=1)
    # article = Article(title='three', content='3', author_id=1)
    # article = Article(title='four', content='4', author_id=1)
    # article = Article(title='five', content='5', author_id=1)
    # article = Article(title='six', content='6', author_id=1)
    # article = Article(title='serven', content='7', author_id=1)
    # article = Article(title='eight', content='8', author_id=1)
    # article = Article(title='nine', content='9', author_id=1)
    # article = Article(title='ten', content='10', author_id=1)
    # db.session.add(article)
    # db.session.commit()  #select * from article;

    user = User.query.filter(User.username == 'zhangsan').first()
    result = user.articles
    for article in result:
        print "-------"
        print article.title

    return 'index page  想要添加一篇文章必须依赖用户而存在,所以首先的话,先添加一个用户'


if __name__ == '__main__':
    app.run(debug=True)