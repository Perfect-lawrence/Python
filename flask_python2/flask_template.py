# -*- coding:utf8 -*-

from flask import Flask,render_template

app = Flask(__name__)


@app.route('/template')
def temp():
    url_str = 'www.b1024.cn'
    my_list = [1,2,354,34,67]
    my_dic = {
        'name': 'lawrence',
        'age': 18,
        'salary': 1000
    }
    return render_template('flask_temp.html',url_str=url_str,my_list=my_list,my_dic=my_dic)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)