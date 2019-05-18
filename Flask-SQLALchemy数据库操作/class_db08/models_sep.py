# encoding:utf-8

from flask import Flask
from models import Article
from exts import db
import config


# 循环引用
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


# db.create_all()




@app.route('/')
def hello_world():
    return "循环引用讲解"


if __name__ == '__main__':
    app.run(debug=True)