# Git笔记

## 搭建仓库

### 创建git仓库

```
git init
```

该命令会在当前目录下创建一个`.git`的隐藏目录，用于进行项目进展的历史记录。

### 克隆仓库

```
git clone ssh://john@example.com/path/to/my-project.git
```

克隆是指将远程仓库拷贝一份到本地，依照这个命令会将仓库复制到my-project目录下。当然克隆命令也可以用在本地其他目标仓库上，不过通常情况下是用来初次复制远程仓库。

### 配置

#### 配置文件

git的配置可以分为3个层级：

1. 本地配置：本地项目的根目录下的`.git/config`文件
2. 全局配置：用户级别的配置，在用户的home目录下`~/.gitconfig`
3. 系统配置：`$(prefix)/etc/gitconfig`

```
git config --global user.email "your_email@example.com"
```

以上通过添加`global`参数来进行全局配置级别。

#### 同名设置

```
git config --global alias.ci commit
```

通过alias可以给原有的命令进行重命名，比如输入`ci`就可以执行`commit`；当然也可以直接在配置文件里修改。


