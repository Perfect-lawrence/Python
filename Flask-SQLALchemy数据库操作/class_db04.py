# encoding:utf8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)


db.create_all()

@app.route('/')
def hello_world():
    # 增加
    blog1 = Blog(title='aaa',content='l love you')
    # add data
    # db.session.add(blog1)
    #
    # db.session.commit()

    # 查
    # res = Blog.query.filter(Blog.title=='aaa').all()
    res = Blog.query.filter(Blog.title == 'aaa').first()
    # tuple_data = res[0]
    # print tuple_data.title
    # print tuple_data.content

    # print 'title: %s' % res.title
    # print 'content: %s' % res.content

    # 改
    # res.title = 'new title'
    # db.session.commit()

    # 删
    db.session.delete(res)
    db.session.commit()

    return 'Blog'




if __name__ == '__main__':
    app.run(debug=True)