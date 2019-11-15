#/usr/bin/env python3
# -*- coding:utf-8 -*-
# pip install psutil


import psutil
psutil.disk_io_counters()  # 返回元组类型
psutil.disk_partitions()  # 返回列表类型
psutil.boot_time()   # 系统启动时间
dir(psutil)  #python dir()函数，获取当前模块的属性列表[dir函数
####1. CPU信息
psutil.cpu_count(logical=False) # cpu物理个数
psutil.cpu_percent() # CPU使用百分比
psutil.cpu_times()
psutil.cpu_times_percent(interval=1, percpu=True/False)
#### mem信息
psutil.swap_memory()   # 返回元组类型
psutil.virtual_memory() # 返回元组类型

#### 磁盘信息
psutil.disk_io_counters()
psutil.disk_usage('/')
psutil.disk_partitions()
psutil.disk_usage('/').percent  # 磁盘使用率

#### 网络和网卡信息
psutil.net_connections()
psutil.net_if_addrs()
psutil.net_if_stats()
psutil.net_io_counters()

#### 用户登录，开机时间
psutil.boot_time()
psutil.users()   # 返回列表类型
len(psutil.users())

#列出当前所有进程的pid
psutil.pids()  # 返回列表类型

#实例化一个Process对象，指定某个进程pid
p = psutil.Process(30661)
''' p.name
Out[74]: <bound method Process.name of psutil.Process(pid=30661, name='dockerd', started='2019-10-11 12:31:31')>
In [81]: p.name() #进程名称
Out[81]: 'dockerd'
In [80]: p.ppid()  #父进程pid
Out[80]: 1
In [82]: p.pid   # 进程pid
Out[82]: 30661

In [84]: p.parent()  #返回父进程，如果不存在父进程，则返回None。
Out[84]: psutil.Process(pid=1, name='systemd', started='2019-07-02 15:23:22')

In [85]: p.parents()  #返回父进程，如果不存在父进程，则返回None。
Out[85]: [psutil.Process(pid=1, name='systemd', started='2019-07-02 15:23:22')]

In [86]: p.exe()   #进程bin路径
Out[86]: '/usr/bin/dockerd'

In [87]: p.cwd   #进程工作目录绝对路径
Out[87]: <bound method Process.cwd of psutil.Process(pid=30661, name='dockerd', started='2019-10-11 12:31:31')>


In [88]: p.username()  #返回哪个用户运行的进程
Out[88]: 'root'

In [89]: p.status   #进程状态
Out[89]: <bound method Process.status of psutil.Process(pid=30661, name='dockerd', started='2019-10-11 12:31:31')>

In [90]: p.status()   #进程状态
Out[90]: 'sleeping'


In [91]: p.create_time() #进程创建时间，时间戳格式
Out[91]: 1570768291.96
In [93]: import datetime

In [94]: datetime.datetime.fromtimestamp(p.create_time())
Out[94]: datetime.datetime(2019, 10, 11, 12, 31, 31, 960000)

In [95]: print( datetime.datetime.fromtimestamp(p.create_time()))
2019-10-11 12:31:31.960000

In [96]: p.uids()  #进程uid信息
Out[96]: puids(real=0, effective=0, saved=0)

In [97]: p.gids()   #进程gid信息
Out[97]: pgids(real=0, effective=0, saved=0)

In [98]: p.cpu_times()   #进程cpu时间信息，包括user和system两个时间。
Out[98]: pcputimes(user=742.69, system=356.65, children_user=5.78, children_system=6.55, iowait=0.01)

In [99]: p.memory_percent()    #进程占用内存利用率百分比
Out[99]: 2.056623534435326

In [100]:  p.memory_info()   #进程内存使用的详细信息
Out[100]: pmem(rss=39653376, vms=526020608, shared=2289664, text=48271360, lib=0, data=396771328, dirty=0)

In [104]: p.io_counters()   #进程的io信息，包括读写io数和字节数

In [106]: p.num_threads()   #进程开启的线程数
Out[106]: 10

In [5]:  p.connections()#返回打开进程socket的namedutples列表，包括fs，family，laddr等信息
Out[5]: []

'''
#### Popen
#####psutil有一个Popen类，可以获取用户启动的应用进程信息，还可以跟踪程序进程的状态
'''
In [110]: pp = psutil.Popen(["/home/xiangxh/py3/bin/python3","-c","print('hello')"],stdout=PIPE)

In [111]: pp.name()
Out[111]: 'python3'

In [112]: pp.username()
Out[112]: 'xiangxh'

In [113]: pp.communicate()
Out[113]: (b'hello\n', None)


'''




 

