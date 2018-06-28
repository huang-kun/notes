# MySQL速查表

## zsh配置

由于在mac上安装了mysql，但是在终端无法使用mysql命令，所以需要修改终端的配置。而我使用zsh，首先`cd ~`，然后`vim .zshrc`，在alias的部分里添加如下配置

```
alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin
alias mysqldump=/usr/local/mysql/bin/mysqldump
```

重启终端后，不仅可以使用mysql，还可以用mysqldump等工具

## 数据库导出导入

#### 数据库导出/备份

```
mysqldump -u [username] –p[password] [参数] [database_name] > [dump_file.sql]
```

注意`-p`和密码之间**不能有空格**

例子：`mysqldump -u mysqltutorial –psecret  classicmodels > /path/to/backup001.sql`

* 只导出数据库结构：添加`–no-data`参数
* 只导出数据，忽略结构：添加`–no-create-info`参数
* 导出多个数据库：`[dbname1,dbname2,…]`
* 导出所有数据库：添加`–all-database`参数

参考 [How To Backup Databases Using mysqldump Tool](http://www.mysqltutorial.org/how-to-backup-database-using-mysqldump.aspx)

#### 数据库导入

```
mysql -u root -p < file.sql
```

## 数据库管理

* 创建数据库`CREATE DATABASE [IF NOT EXISTS] database_name;`
* 显示数据库`SHOW DATABASES;`
* 选择数据库`USE database_name;`
* 删除数据库`DROP DATABASE [IF EXISTS] database_name;`

#### 表管理

在此前，首先要选择数据库！

* 显示所有表`SHOW TABLES;`
* 查看表结构/描述`DESCRIBE table_name`
* 查看创建语句`SHOW CREATE TABLE table_name`
* 删除表`DROP table_name`

导出全部表结构`mysqldump -u [user] -p [database_name] --compact --no-data`

#### 创建

```
CREATE TABLE IF NOT EXISTS tasks (
  task_id INT(11) NOT NULL AUTO_INCREMENT,
  subject VARCHAR(45) DEFAULT NULL,
  start_date DATE DEFAULT NULL,
  end_date DATE DEFAULT NULL,
  description VARCHAR(200) DEFAULT NULL,
  PRIMARY KEY (task_id)
) ENGINE=InnoDB
```

#### 更改表结构

```
ALTER TABLE tasks
CHANGE COLUMN task_id task_id INT(11) NOT NULL AUTO_INCREMENT;
```

#### 添加字段

```
ALTER TABLE tasks 
ADD COLUMN complete DECIMAL(2,1) NULL
AFTER description;
```

#### 删除字段

```
ALTER TABLE tasks
DROP COLUMN description;
```

#### 表重命名

```
ALTER TABLE tasks
RENAME TO work_items;
```

参考 [Using MySQL ALTER TABLE To Change Table Structure](http://www.mysqltutorial.org/mysql-alter-table.aspx)
