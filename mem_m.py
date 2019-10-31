#!/usr/bin/env python
# -*- coding:utf-8 -*- 

from __future__ import division 
import re,time
localtime = time.asctime(time.localtime(time.time()))
def mem_stat():
    f = open('/proc/meminfo')
    lines = f.readlines()
    f.close()
    memtotal = re.findall(r"\d+",lines[0])
    mem_total = "".join(memtotal)
    memfree = re.findall(r"\d+",lines[1])
    mem_free = "".join(memfree)
    membuffers = re.findall(r"\d+",lines[3])
    mem_buffers = "".join(membuffers)
    memcache = re.findall(r"\d+",lines[4])
    mem_cache = "".join(memcache)
    mem_usage_per = (int(mem_free) + int(mem_buffers) + int(mem_cache))/int(mem_total)*100
    mem_free_per = int(mem_free)/int(mem_total)*100
    print("%s  内存使用率(free/total):%s,内存占用率:%s" %(localtime,mem_free_per,mem_usage_per))
mem_stat()
