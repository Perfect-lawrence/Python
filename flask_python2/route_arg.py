# -*- coding:utf8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/order/<order_id>')
def get_order_id(order_id):
    return 'order_id %s' % order_id

# # 转换成 int类型
@app.route()
def get_order_id('/order/<int:order_id>'):
    print(type(order_id))
    return "order_id：%s" % order_id

# 转换成 float类型
@app.route()
def get_order_id('/order/<float:order_id>'):
    print(type(order_id))
    return "order_id：%s" % order_id

if __name__ == "__main__":
    app.run()