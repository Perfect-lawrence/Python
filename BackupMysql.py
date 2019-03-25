#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import time
import datetime
import sys
"""
cat /data/pycharm_python3/mysql_backup/dbname.txt
xiaohai
mysql
dev_django

"""
DB_NAME_LIST = '/data/pycharm_python3/mysql_backup/dbname.txt'
BACKUP_PATH = '/data/pycharm_python3/mysql_backup/'

DATETIME = time.strftime('%Y%m%d_%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + DATETIME

# 这里可以加上出路异常，如果没有权限
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)
    print("创建备份目录成功")
def start_backup():
    if os.path.exists(DB_NAME_LIST):
        backupdbs = open(DB_NAME_LIST,'r')

    for dbs in backupdbs.readlines():
        dbname = dbs.strip()
        print("start backup database %s" % dbs)
        mysql_dump = "/usr/local/mysql/bin/mysqldump --defaults-file={0} --host={1} --user={2} --password={3} --port={4}  --max-allowed-packet={5} --master-data={6} -B {7} --quick --routines  --events --comments --single-transaction  --set-gtid-purged={8} {9} {10}/{11}.sql  ".format('/etc/my.cnf','localhost','root','12345678',3388,'128M',2,dbname,'OFF','>',TODAYBACKUPPATH,dbname)
        os.system(mysql_dump)
        #print(mysql_dump)
    backupdbs.close()
    return 'successful'

def start_tar():
    tar_file = TODAYBACKUPPATH + ".tar.gz"
    tar_cmd = "tar -czvf" +tar_file+ " " +DATETIME
    os.chdir(BACKUP_PATH)
    #os.system("pwd")
    os.system(tar_cmd)
    # 删除 备份文件
    if os.listdir(TODAYBACKUPPATH):
        os.chdir(BACKUP_PATH)
        #os.system("rm -rf " +TODAYBACKUPPATH)
        os.system("rm -rf " + DATETIME)
#start_backup()
    return


if __name__ == "__main__":
    if os.path.exists(DB_NAME_LIST):
        backupdbs = open(DB_NAME_LIST, 'r')
        print("starting backup db list: " +DB_NAME_LIST)
        start_backup()
        start_tar()
        print("backup success !")
        backupdbs.close()
    else:
        print("backup database failed")
        sys.exit()
