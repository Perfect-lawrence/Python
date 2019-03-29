#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import psutil


def netstat():
    status_list = ["LISTEN", "ESTABLISHED", "TIME_WAIT", "CLOSE_WAIT", "LAST_ACK", "SYN_SENT"]
    status_temp = []

    net_connections = psutil.net_connections()
    for key in net_connections:
        status_temp.append(key.status)

    for status in status_list:
        print(status, status_temp.count(status))
        #sta, conn = status, status_temp.count(status)
    #return sta, conn
    return 
# 指定查看某个端口连接数
def conn_nums(sport=None):
    status_list = ["LISTEN", "ESTABLISHED", "TIME_WAIT", "CLOSE_WAIT", "LAST_ACK", "SYN_SENT"]
    status_temp = []
    net_connections = psutil.net_connections()
    for key in net_connections:
        if sport is None:
            status_temp.append(key.status)
        else:
            if key.laddr[1] == sport:
                status_temp.append(key.status)

    for status in status_list:
        print(status, status_temp.count(status))
        #stat,conn2 = status, status_temp.count(status)
    # return stat,conn2
    return 


if __name__ == "__main__":
    netstat()
    conn_nums(22)
