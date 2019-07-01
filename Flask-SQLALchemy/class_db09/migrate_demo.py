# encoding:utf-8

from flask import Flask
from exts import db
import config
from models import Article

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# source venv/bin/activate
# pip install flask-migrate
# pip list


# 新建一个article模型，采用models分开的方式
# flask-scripts的方式
# with app.app_context():
#     db.create_all()

@app.route('/')
def hello_world():

    return ' Flask_Migrate Models '


if __name__ == '__main__':
    app.run(debug=True)