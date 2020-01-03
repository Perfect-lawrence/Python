#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import time

if len(sys.argv)>1:
	INTERFACE =sys.argv[1]
else:
	INTERFACE = "eth0"

print "当前查看的网卡为:",INTERFACE
sta =[]

def  rx(): 
	ifstat =open("/proc/net/dev").readlines()
	for interface in ifstat:
		if INTERFACE in interface:
			stat = float(interface.split()[1])
			sta[0:]=[stat]


def tx():
	ifstat =open("/proc/net/dev").readlines()
	for interface in ifstat:
		if INTERFACE in interface:
			stat = float(interface.split()[9])
			sta[1:]=[stat]


if __name__ == '__main__':
	print "IN" ,">"*10  ,"OUT"
	rx()
	tx()
	while 1:
		time.sleep(1)
		stat_0 =list(sta)
		rx()
		tx()
		RX =float(sta[0])
		RX_0=stat_0[0]
		TX =float(sta[1])
		TX_0 =stat_0[1]
		RX_INFO =round((RX-RX_0)/1024/1024,3)
		TX_INFO =round((TX-TX_0)/1024/1024,3)
		print RX_INFO,"'Mb",TX_INFO,"Mb"

