# 在Ubuntu16.04安装Python3.6.5


#### 安装依赖环境

```
apt-get install openssl  
apt-get install libssl-dev
apt-get install libc6-dev gcc  
apt-get install -y make build-essential zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm tk-dev 
```


#### 从Python官网下载源码包

```
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
```


#### 解压文件

```
tar -xvf Python-3.6.5.tar.xz
```


#### 进入文件目录

```
cd Python-3.6.5
```


#### 添加配置

```
./configure --prefix=/usr/Python-3.6.5
```


#### 编译源码

```
make
```


#### 安装

```
make install
```


#### 添加快捷运行程序/软连接

`ln -s <当前安装的Python可执行程序路径> /usr/bin/python`

`/usr/bin/python`是系统默认安装的Python程序，版本是2.7，如果执行命令的话，会覆盖默认版本；
如果不打算覆盖Python 2.7的程序，可以换成`/usr/bin/python3`，安装好以后即在终端执行`python3`就可以运行Python 3.6.5

比如我把Python 3.6.5 安装在了root文件下，于是执行

```
ln -s /root/Python-3.6.5/python /usr/bin/python3
```


# 解决pip错误

我在Ubuntu使用`pip install xxx`的时候，发现出错`'lsb_release -a' returned non-zero exit status 1`，后来找到解决方案是因为这个文件`/usr/bin/lsb_release`，网上说该文件默认是使用Python 3来实现的，但是lsb_release却需要Python 2的环境，因此需要：

1. 将文件`/usr/bin/lsb_release`文件的首行改为`#! /usr/bin/python2.7`
2. 保存后继续执行`pip install xxx`，如果出错并且错误指向该文件的语法问题的话，那么还需要将该文件的语法适配到Python 2.7的语法，修改后保存再次执行`pip install`，不出意外应该能成功

参考[pip is showing error 'lsb_release -a' returned non-zero exit status 1](https://stackoverflow.com/questions/44967202/pip-is-showing-error-lsb-release-a-returned-non-zero-exit-status-1)
