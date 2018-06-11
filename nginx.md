nginx学习笔记

## 路径

* nginx应用程序的安装路径在`/usr/local/Cellar/nginx`文件夹内，其中是安装的版本，比如`1.15.0`，实际的可执行文件在`1.15.0/bin`目录中
* nginx的配置文件是`nginx.conf`，该文件可能存在的地方包含：
	* `/usr/local/nginx/conf`
	* `/etc/nginx`
	* `/usr/local/etc/nginx`
* 默认root路径`/usr/local/var/www`，该目录下默认有主页`index.html`和错误页`50x.html`
* 默认log路径`/usr/local/var/log/nginx`，该目录下有访问日志`access.log`和错误日志`error.log`

## 访问静态文件

```
location /images/ {
	root /data;
}
```

使用其他默认设置，访问`http://localhost:8080/images/hill.png`，于是nginx会查找本地文件`/data/images/hill.png`