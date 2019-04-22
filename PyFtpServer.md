# python3 快速搭建FTP服务器
 * 安装第3方库
 
```
pip3 install pyftpdlib
```
* 建立上传ftp 家目录
 
```
 mkdir -v /home/xiangxh/pyftpserver
  cd Py3_virtualenv/
  source bin/activate
```

* 开始搭建ftp服务器
 
```
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer



authorizer = DummyAuthorizer()
authorizer.add_user("xiangxh","123456","/home/xiangxh/pyftpserver",perm="elradfmw")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("192.168.5.6",20231),handler)
server.serve_forever()

```

* 启动ftp服务器

```
$ python FtpServer.py 
[I 2019-04-22 16:21:53] >>> starting FTP server on 192.168.5.6:20231, pid=7604 <<<
[I 2019-04-22 16:21:53] concurrency model: async
[I 2019-04-22 16:21:53] masquerade (NAT) address: None
[I 2019-04-22 16:21:53] passive ports: None
[I 2019-04-22 16:24:14] 192.168.1.221:49200-[] FTP session opened (connect)
[I 2019-04-22 16:24:14] 192.168.1.221:49200-[xiangxh] USER 'xiangxh' logged in.
[I 2019-04-22 16:24:14] 192.168.1.221:49200-[xiangxh] CWD /home/xiangxh/pyftpserver/home/xiangxh/pyftpserver 550 'No such file or directory.'
[I 2019-04-22 16:24:42] 192.168.1.221:49200-[xiangxh] STOR /home/xiangxh/pyftpserver/auth.go completed=1 bytes=10662 seconds=0.023
[I 2019-04-22 16:24:42] 192.168.1.221:49200-[xiangxh] MFMT /home/xiangxh/pyftpserver/auth.go 550 'Not enough privileges.'
[I 2019-04-22 16:25:10] 192.168.1.221:49200-[xiangxh] FTP session closed (disconnect).


```
 
*  文件上传结果

```
[xiangxh@paojiao pyftpserver]$ pwd
/home/xiangxh/pyftpserver
[xiangxh@paojiao pyftpserver]$ ls -lh
total 60K
-rw-rw-r-- 1 xiangxh xiangxh  11K Apr 22 16:24 auth.go
-rw-rw-r-- 1 xiangxh xiangxh  41K Apr 22 16:19 auth_test.go
-rw-rw-r-- 1 xiangxh xiangxh 3.6K Apr 22 16:21 const.go

```
