
### mysql8数据库连接失败

估计是更新了安全性？这里通过重设原密码来恢复登录

登录mysql

```
mysql -u root -p
```

选择mysql表

```
use mysql
```

重新赋值密码

```
alter user 'user_name'@'localhost' identified with mysql_native_password by 'new_password' password expire never;
```

