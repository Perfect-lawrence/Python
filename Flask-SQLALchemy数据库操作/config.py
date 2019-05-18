# coding:utf-8

# dialect+driver://username:password@host:port/database

DIALECT = 'mysql'
DRIVER = 'mysqldb'
# USERNAME = 'lawrence'
USERNAME = 'root'
PASSWORD = '1qaz2wsx'
# HOST = '127.0.0.1'
HOST = 'localhost'
PORT = '3306'
#DATABASE = 'db_demo1'

# DATABASE = 'db_demo2'
# DATABASE = 'db_demo3'
# DATABASE = 'db_demo4'
DATABASE = 'db_demo5'


SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False