# encoding:utf-8


# import os
DIALECT = 'mysql'
DRIVER = 'mysqldb'
HOSTNAME = 'localhost'
PORT =  3306
DATABASE = 'db_demo5'
USERNAME =  'root'
PASSWORD = '1qaz2wsx'
# DB_URI = 'mysql +mysqldb://{}:{}@{}:{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
#
# SQLALCHEMY_DATABASE_URI =  DB_URI
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = True

# DEBUGE = True