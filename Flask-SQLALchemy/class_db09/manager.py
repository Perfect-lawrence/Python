# encoding:utf-8

from flask_script import Manager
from migrate_demo import app
from flask_migrate import Migrate,MigrateCommand
from exts import db
from models import Article


manager = Manager()
# 1.要使用flask_migrate,必须绑定app和db
migrate = Migrate(app,db)

# 2 把 MigrateCommand命令添加到manager中
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()