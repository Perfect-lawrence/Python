# encoding:utf-8

from flask_script import Manager
from class_db07 import app
from db_script import DBmanager
manager = Manager(app)



#
@manager.command
def runserver():
    print "start server ......."


manager.add_command('db',DBmanager)
if __name__ == '__main__':
    manager.run()


    # python manager.py db init
    # python manager.py db migrate