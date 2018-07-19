# Git笔记

## Getting Started

### Setting up a repository

#### init

该命令会在当前目录下创建一个`.git`的隐藏目录，用于进行项目进展的历史记录。

#### clone

```
git clone ssh://john@example.com/path/to/my-project.git
```

克隆是指将远程仓库拷贝一份到本地，依照这个命令会将仓库复制到my-project目录下。当然克隆命令也可以用在本地其他目标仓库上，不过通常情况下是用来初次复制远程仓库。

#### config

**配置文件**

git的配置可以分为3个层级：

1. 本地配置：本地项目的根目录下的`.git/config`文件
2. 全局配置：用户级别的配置，在用户的home目录下`~/.gitconfig`
3. 系统配置：`$(prefix)/etc/gitconfig`

```
git config --global user.email "your_email@example.com"
```

以上通过添加`global`参数来进行全局配置级别。

**alias**

```
git config --global alias.ci commit
```

通过alias可以给原有的命令进行重命名，比如输入`ci`就可以执行`commit`；当然也可以直接在配置文件里修改。

### Saving changes

#### add

将改动从`working area`添加到`staging area`，可以添加文件、目录，甚至只添加部分改动。`staging area`就好比一个缓冲区`buffer`，存放着一些还没有准备好提交的改动。

#### commit

将`staging area`的所有改动创建出一个`snapshot`提交到`history`中，成为git历史时间线中的一个组成节点。git的提交非常高效，相比于svn的提交（每次只记录改动部分），git的每次提交都会记录整个文件的内容，即`snapshot`。

添加参数`--amend`可以允许修改最近一次的提交，修改后的提交时间仍然不变。

#### diff

* `git diff HEAD <file>`对比文件在工作区里修改前后的区别，其中`HEAD`可以省略。
* 如果改动被添加到`staging area`的话，也可以通过参数`--cached`或`--staged`来查看`staging area`中文件的改动区别。
* `git diff <commit_id> <next_commit_id>`可以查看两次提交的改动区别，中间可以是空格或者`..`符号
* `git diff <branch1> <branch2>`查看分支区别
* `git diff master new_branch ./diff_test.txt`查看文件在不同分支里的区别

#### stash

如果想保存修改但是又不至于提交的话，可以用`git stash`将`working area`和`staging area`的修改全部保存起来，立即呈现出一个干净的工作区。可以把`stash`想象成桌边角落的耸立起来的“书堆“，把桌子上不用的东西先堆在上面，方便归置凌乱的书桌。

使用`git stash pop`即可恢复现场，并且把数据从“书堆“上清理出来。

使用`git stash apply`也可以恢复现场，但是数据也会保留在“书堆“上，这样相同的数据就可以应用到不同的分支上。

`stash`默认保存git追踪的文件，但是也可以适用于未追踪和`.gitignore`中的文件：

* 参数`-u`或者`--include-untracked`就可以保存未追踪的文件
* 参数`-a`或者`--all`即可保存`.gitignore`中的文件

`stash`可以保存多个现场，每一个保存的现场被称为`WIP`(work in progress)，可以使用`git stash list`查看保存的列表。最近一次保存的被放置在栈顶，它的id被写成`stash@{0}`，也是`git stash pop`首先中栈里取出的现场。通过id可以指定取出某个现场，比如`git stash pop stash@{2}`；为了方便理解保存的信息或者原因，推荐使用`git stash save "..."`来添加一些描述。

通过`git stash show`可以查看保存现场的diff区别，添加`-p`或者`--patch`参数即可查看完整的diff细节。

直接使用`git stash -p`可以实现部分保存，git会在每个小改动的地方都会询问是否需要保存起来，具体回复操作[参考这里](https://www.atlassian.com/git/tutorials/saving-changes/git-stash)

如果保存改动后，做了新的修改，但是应用之前的保存的话，万一冲突怎么办？可以通过`git stash branch <new_branch_nane> stash@{n}`从保存的节点处新创建一个分支，把先前保存的现场pop到新的分支里。

对于不再需要的现场，可以用`git stash drop stash@{n}`来清除掉，或者`git stash clear`清空所有。


#### gitignore

通过在git追踪的项目主目录下添加`.gitignore`文件，来忽略对某些文件的追踪。具体的匹配模式[查看这里](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)。此外也可以自己设置ignore规则，强制提交被忽略的文件等等。还可以通过`git check-ignore -v <file_path>`来检查某个文件是否匹配到忽略文件列表中。

### Inspecting a repository

#### status

显示`working area`, `staging area`的状态，以及没有追踪的文件。

#### log

显示提交历史

* `-n <limit>`限制个数
* `--oneline`单行显示（缩减版id）
* `--pretty=oneline`单行显示
* `--stat`显示改动文件与行数
* `-p`显示全部细节
* `--author="<pattern>"`按作者名查找，也可以使用正则表达式
* `--grep="<pattern>"`查找提交的message查找，也可以使用正则表达式
* `<since>..<until>`给定区间查找，可以是commit_id，分支名称或者HEAD
* `<file>`查看某个文件的提交历史
* `--graph --decorate --oneline`图形组合

可以使用`~`表示某个提交之前/上n个提交，比如`HEAD~1`表示最近一次提交的上一次提交；`586f91e~3`表示id为586f91e的提交前面的第三个提交。


#### tag

标记某个提交（打标签），通常用于标记发布版本

* 创建标签就是`git tag <tagname>`，即给当前的最新提交打个标签
* tag分为两种类型：
	* `Annotated tag`：用于公开，可包含多个元信息：名称、邮箱、日期
		* `git tag -a v1.4 -m`可以添加额外备注
	* `Lightweight tag`：只要不带`-a -s -m`等参数的都算
		* `git tag v1.4`
* `git tag`可以查看标签列表，参数`-l`可以匹配通配符，比如`git tag -l *-rc*`就匹配出带有-rc的版本号
* `git tag <tagname> <commit_id>`可以为某个提交打标签
	* 如果重复打同名标签的话就会失败，可以通过`-f`参数来强制更新某个提交的标签
	* 比如`git tag -a -f <tagname> <commit_id>`
* `-d`删除标签

使用`git push`默认不会把本地tags推送到远程，需要添加参数`git push --tags`；而`pull`或`clone`操作会把远程的tags同步到本地。

`git checkout <tagname>`会将HEAD设置成分离的状态，之后的任何改动都不会改变那个tag下的提交，改动后保存的提交不会归属于任何一个分支，只能通过查找id的方式来追溯，不过推荐将在此之后的改动创建为新的分支。


#### blame

### Undoing changes

#### checkout

#### clean

#### revert

#### reset

### Rewriting history

#### commit --amend

#### rebase

#### rebase -i

#### reflog

## Collaborating

### Syncing

#### remote

#### fetch

#### push

#### pull

### Making a pull request

### Using branches

#### branch

#### checkout

#### merge

### Comparing workflows

## Advanced Tips

### Merging vs. Rebasing

### Resetting, checking out and reverting

### Advanced git log

### Git hook

### Refs and Reflog

### Git LFS

## 参考

[atlassian git tutorial](https://www.atlassian.com/git/tutorials)
