# encoding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'SQLAlchemy mysql-python'

db.create_all()

if __name__ == '__main__':
    app.run()
