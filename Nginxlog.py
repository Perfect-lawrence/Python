#!/usr/bin/env python
# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding:utf8 -*-

ips = {}
fh = open("/home/xiangxh/access_2018-07-24.log","r").readlines()
for line in fh:
    ip = line.split(" ")[0]
    if 6 < len(ip) <=15:
        ips[ip] = ips.get(ip,0) + 1
print(ips)

