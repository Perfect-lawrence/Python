python虚拟环境--virtualenv 
=====
- 安装
```
pip install virtualenv
```
- 为一个工程创建一个虚拟环境
```
mkdir my_project_dir  && cd my_project_dir

/usr/bin/virtualenv  -p /usr/bin/python2.7 my_project_dir/flask2  # -p参数指定Python解释器程序路径
/usr/local/python367/bin/virtualenv -p /usr/local/python367/bin/python3 my_project_dir/flask3
```
- 进入虚拟环境，其需要被激活：
```
$ source venv/bin/activate　
```
- 你现在使用pip安装的包将会放在 flask 文件夹中，与全局安装的Python隔绝开。
像平常一样安装包：
```
$ pip install flask
```
- 退出虚拟环境：
```
$ . venv/bin/deactivate
```
- 要删除一个虚拟环境，只需删除它的文件夹。（执行 rm -rf flask2 ）。

- 这里virtualenv 有些不便，因为virtual的启动、停止脚本都在特定文件夹，可能一段时间后，你可能会有很多个虚拟环境散落在系统各处，你可能忘记它们的名字或者位置。
virtualenvwrapper
- 鉴于virtualenv不便于对虚拟环境集中管理，所以推荐直接使用virtualenvwrapper。 virtualenvwrapper提供了一系列命令使得和虚拟环境工作变得便利。它把你所有的虚拟环境都放在一个地方。
- 安装virtualenvwrapper(确保virtualenv已安装)
```
pip install virtualenvwrapper
pip install virtualenvwrapper-win　　#Windows使用该命令
```
- 安装完成后，在~/.bashrc写入以下内容
```
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
```
- 第一行：virtualenvwrapper存放虚拟环境目录
- 第二行：virtrualenvwrapper会安装到python的bin目录下，所以该路径是python安装目录下bin/virtualenvwrapper.sh
```
source ~/.bashrc　　　　#读入配置文件，立即生效
```
- virtualenvwrapper基本使用
- 创建虚拟环境　mkvirtualenv
```
mkvirtualenv flask3　
```
- 这样会在WORKON_HOME变量指定的目录下新建名为flask的虚拟环境。
- 若想指定python版本，可通过"--python"指定python解释器
```
mkvirtualenv --python=/usr/local/python367/bin/python3 flask3
```
- 基本命令 　
- 查看当前的虚拟环境目录
```
[root@localhost ~]# workon
flask2
flask3
```
- 切换到虚拟环境
```
[root@localhost ~]# workon flask3
(flask3) [root@localhost ~]# 
```
- 退出虚拟环境
```
(flask3) [root@localhost ~]# deactivate
[root@localhost ~]# 
```
- 删除虚拟环境
```
rmvirtualenv flask3
```
