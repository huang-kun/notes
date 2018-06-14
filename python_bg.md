
## Ubuntu后台启动python脚本：

`nohup python3 -u main.py > log.txt 2>&1 &` 后台运行main.py的程序

返回一个pid，比如`[1] 15546`

## 查看后台运行中的程序

`ps -ef | grep python` 这里只显示python程序

```
root     15546 15500  0 14:19 pts/0    00:00:00 python3 -u main.py
root     15548 15500  0 14:19 pts/0    00:00:00 grep --color=auto python
```

## 销毁程序

`kill -9 15546`

## 参考：

[在Ubuntu下后台持续运行Python程序](https://blog.csdn.net/mrbcy/article/details/64533496)