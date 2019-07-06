# -*- coding:utf8 -*-

#

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index/',methods=['GET','POST'])
def index():
    return render_template('index.html')



@app.route('/order/<order_id>')
def get_order_id(order_id):
    return 'order_id %s' % order_id

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
