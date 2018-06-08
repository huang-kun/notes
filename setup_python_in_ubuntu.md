在Ubuntu16.04安装Python3.6.5


#### 安装依赖环境

```
sudo apt-get install openssl  
sudo apt-get install libssl-dev
sudo apt-get install libc6-dev gcc  
sudo apt-get install -y make build-essential zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm tk-dev 
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
