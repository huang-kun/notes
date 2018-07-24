# Git笔记

## Getting Started

git中的3大区域：

* `working`区域
* `staging`区域
* `commit`历史

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

* `-m`或`--message`编辑提交信息，不带该参数的话，就会弹出默认编辑框
* `--amend`可以允许修改最近一次的提交，修改后的提交时间仍然不变。
* `--allow-empty`可以保存一次空的提交

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

用于查看文件的每一行/段内容最后是谁来编辑/修改的。`git blame`可以查看使用帮助，通常该命令格式为`git blame [参数] <file>`


### Undoing changes

git里的回退/撤销有以下方法：

* `git checkout <old_commit>`查看之前的提交，不会改变历史
* `git revert`适合在多人协作的公共分支上进行回退，不会改变历史
* `git reset`适合在自己本地的分支里进行回退，会改变历史
* 如果最后一次提交不够全面的话，可以`git commit --amend`来修改它
* 对于撤销`staging area`的修改，可以`git reset --mixed`
* 对于撤销`working area`的修改，可以`git clean`或者`git checkout -- <file>`

#### checkout

`git checkout <commit_id>`查看某个提交，该行为会让`HEAD`指针移动到指定提交的位置，该行为会造成`detached HEAD`状态，即`HEAD`指针与`branch`指针的位置分离了。在该状态下，可以随意查看、修改、生成新的提交，而且不会影响到任何分支，由于这些新提交不属于任何一个分支，因此它们被看作是`Orphaned`，这样它们就会在切回分支的时候被垃圾回收给清理掉，好像不存在过一样。如果想保留这些新提交的话，就需要在此节点上建立一个新的分支，来维持它们的存在。

`git checkout <file>`与之不同，它只是查看旧版本的文件，并没有移动`HEAD`指针的位置，所以不会造成`detached HEAD`状态。

#### clean

该命令是删除未被git追踪的文件，使用的话必须使用参数：

* `-n`会执行一个`dry run`，相当于从git中删除，但不会真正删除实际文件
* `-f`会执行删除命令，删除项目中没有被git追踪的文件
  * `git clean -f <path>`删除指定某个文件
* `-d`指定操作对象仅为目录，可以和上面的参数联合使用，比如`-dn`,`-df`
* `-x`指定操作对象为`.gitignore`里所有的文件
* `-i`交互模式

#### revert

该命令会重置某次提交的内容，然后将该行为作为一次新的提交记录下来，而被重置的提交依然保存在之前的历史中。使用时需要指定位置信息，比如`git revert HEAD`或者`git revert <commit_id>`

* `-e`或`--edit`打开编辑器，是默认行为
* `--no-edit`不会打开编辑器
* `-n`或`--no-commit`不会提交的撤销，即撤销到提交前的`staging area`

需要特别注意的是：

1. `revert`不会改变历史，只可能增加历史节点
2. `revert`只是重制单个提交的内容，不包含那次提交后面至今的所有历史

#### reset

`git reset [参数] [文件路径/指针位置/commit_id]`进行撤销操作，将历史回退到某个节点。

之前提到的`checkout`只是移动`HEAD`指针指向某个历史提交位置，`branch`指针的位置不变，所以保留了分支里所有历史信息。而`reset`通过移动`HEAD`和`branch`两个指针到指定的提交位置，把回退的位置作为历史最新的节点，这样之后的所有提交就被“丢弃”了。

* `--hard`将回退`working`,`staging`,`commits`3个区域到指定的历史节点，来还原当时的情景，因此**会丢弃`working`和`staging`区域下的全部改动**，也被视为危险操作
* `--mixed`将回退`staging`,`commits`2个区域到指定的历史节点，因此在`staging`下的改动会返回到`working`区域
* `--soft`只回退`commits`区域到指定的历史节点，多余的改动保留进了`staging`区域，而`working`区域保持不变

`git reset`等同于`git reset --mixed HEAD`，即撤销到最近一次的提交历史，并且将`staging`区域的改动返回至`working`区域。

#### rm

`git rm`用来删除被git追踪的文件，相当于执行`rm`和`git add`两步操作，即删除文件后接着加入到`staging`区准备下一次提交。

* 可以删除多个文件或目录或通配符，比如`git rm file1 file2`, `git rm Folder/*`
* `-f`或`--force`强制删除，如果被删除的文件此时在`staging`区域的话，普通删除就会被阻止
* `-n`或`--dry-run`调试模式，只是打印删除结果，不会真正删除文件
* `-r`递归删除文件目录下的文件，但不会删除目录
* `--cached`将`staging`区的文件从git追踪里删除，但仍会保留修改后的文件在磁盘里
* 其他参数可以参考文档

### Rewriting history

#### commit --amend

修改最后一次提交的情况和方法：

* 提交信息写错了怎么办？
	* `git commit --amend -m '在这里更新最后一次提交的信息'`
* 提交后发现遗漏了一个文件怎么办？
	1. `git add <遗漏文件>`
	2. `git commit --amend --no-edit`可以在不修改提交信息的情况下修改提交

**不要用`--amend`修改已经放在远程的提交**，不然也会影响到其他开发人员

#### rebase

`rebase`是将一系列提交移动或整合到一个新的提交的基础上，说白话就是转移基地。常见的实用案例：

1. 在当前master上开个分支做新功能，之后又再master上更新了bug修复，这时候两个分支都分别有了自己的提交记录，于是开始走向分岔了；而在新功能分支上使用rebase就可以从master分支里将开启该分支的起点重置到bug修复的位置，这样既享受了最新master的进展，又能保持功能分支干净的历史线（减少合并的必要）
2. 在自己功能分支上写了很多提交后，发现提交又多又乱，可以使用rebase来规整一下，合并或排序提交，保持一个干净整洁的提交历史，然后再合并到主干/共享分支上，方便别人code review

`rebase`主要有两个模式：

1. `git rebase`是自动模式，可以自动将当前分支里的所有提交应用到基于它的基础分支的HEAD位置
2. `git rebase -i`开启交互模式，即手动操作每个提交

**注意事项**：

* `rebase`的实现其实是在新的基础节点上创建新的提交，因此rebase后基于新节点开始的所有提交的id都会发生更新。
* `rebase`其实也是修改历史的操作，所以不建议用在远程/多人协作的分支上，避免出现历史节点缺失或冲突等问题。


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
