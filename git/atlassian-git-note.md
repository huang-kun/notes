# Git笔记


## Getting Started

**git中的3大区域**：

* `working`区域
* `staging`区域
* `commit`历史

**Detached HEADS**：

这是一种指针分离的状态，意思是在该状态下的指针位置与当前项目开发的分支环境已经分离，在该状态下对项目进行改动都不属于任何分支，回到原先项目节点后将不会在历史中显示在分离状态下的改动（除非手动创建分支来追踪他们）。

**转义符号**

`--`将其后面的参数转义成文件名来处理，[参考这里](https://segmentfault.com/q/1010000006723213?_ea=1113161)


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
	* `git log -n 1 <tagname>`可以看到tag对应的commit_id
* `git tag <tagname> <commit_id>`可以为某个提交打标签
	* 如果重复打同名标签的话就会失败，可以通过`-f`参数来强制更新某个提交的标签
	* 比如`git tag -a -f <tagname> <commit_id>`
* `-d`删除本地标签
	* 如果要删除远程标签的话，首先要删除本地标签，然后把结果同步到远程`git push origin :refs/tags/<deleted_tagname>`

使用`git push`默认不会把本地tags推送到远程，需要添加参数`git push --tags`；而`pull`或`clone`操作会把远程的tags同步到本地。

`git checkout <tagname>`会将HEAD设置成分离的状态，之后的任何改动都不会改变那个tag下的提交，改动后保存的提交不会归属于任何一个分支，只能通过查找id的方式来追溯，不过推荐将在此之后的改动创建为新的分支。

如果需要查看`Annotated tag`的细节信息/笔记的话，可以使用`git tag -n9`查看所有tags的信息；或者`git tag -l -n9 v3.*`通配符来匹配特定版本的信息/笔记。

#### blame

用于查看文件的每一行/段内容最后是谁来编辑/修改的。`git blame`可以查看使用帮助，通常该命令格式为`git blame [参数] <file>`


### Undoing changes

git里的回退/撤销有以下方法：

* `git checkout <old_commit>`查看之前的提交，不会改变历史
* `git revert`适合在多人协作的公共分支上进行回退，不会改变历史
* `git reset`适合在自己本地的分支里进行回退，会改变历史
* 如果最后一次提交不够全面的话，可以`git commit --amend`来修改它
* 对于撤销`staging area`的修改，可以`git reset --mixed`
* 对于撤销`working area`的修改，可以`git checkout -- <file>`


#### checkout

`git checkout <commit_id>`查看某个提交，该行为会让`HEAD`指针移动到指定提交的位置，该行为会造成`detached HEAD`状态，即`HEAD`指针与`branch`指针的位置分离了。在该状态下，可以随意查看、修改、生成新的提交，而且不会影响到任何分支，由于这些新提交不属于任何一个分支，因此它们被看作是`Orphaned`，这样它们就会在切回分支的时候被垃圾回收给清理掉，好像不存在过一样。如果想保留这些新提交的话，就需要在此节点上建立一个新的分支，来维持它们的存在。通过`git checkout <branch>`回到最近的进度。

`git checkout <file>`与之不同，它只是查看旧版本的文件，并没有移动`HEAD`指针的位置，所以不会造成`detached HEAD`状态。


#### clean

该命令是删除未被git追踪的文件，使用的话必须使用参数：

* `-n`或`--dry-run`会执行调试模式，打印出所有删除的文件，但不会真正删除实际文件
* `-f`会执行删除命令，删除项目中没有被git追踪的文件
  * `git clean -f <path>`删除指定某个文件
* `-d`指定操作对象仅为目录，可以和上面的参数联合使用，比如`-dn`,`-df`
* `-x`指定操作对象为`.gitignore`里所有的文件
* `-i`交互模式

总结：罗列出所有未被git追踪的文件和目录`git clean -fdn`，如果没有问题的话，去掉参数`n`就可以真正执行删除了。

#### revert

该命令会重置某次提交的内容，然后将该行为作为一次新的提交记录下来，而被重置的提交依然保存在之前的历史中。使用时需要指定位置信息，比如`git revert HEAD`或者`git revert <commit_id>`

* `-e`或`--edit`打开编辑器，是默认行为
* `--no-edit`不会打开编辑器
* `-n`或`--no-commit`不会提交的撤销，即撤销到提交前的`staging area`

需要特别注意的是：

1. `revert`不会改变历史，只可能增加历史节点
2. `revert`只是重制单个提交的内容，不包含那次提交后面至今的所有历史


#### reset

`git reset [参数] [指针位置/commit_id]`进行撤销操作，将历史回退到某个节点；它可以回退某个文件的状态，比如`git reset <file>`。

之前提到的`checkout`只是移动`HEAD`指针指向某个历史提交位置，不会改变当前分支末端的位置，所以保留了分支里所有历史信息。而`reset`移动当前分支末端的位置到指定的提交位置，因此这里就成为历史最新的节点`HEAD`，该节点之后的所有提交就被“丢弃”了。

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


#### reflog

[查看网页](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog)


## Collaborating


### Syncing


#### remote

`remote`可以管理本地repo与其他repo的连接，方便用于多人协作。它设置了一个`<name> - <repo_url>`的关系，即通过简短的名称来访问其远程的URL地址。它本质是通过命令来读取或修改项目中的`.git/config`的远程配置等相关信息，因此即便忽略相关命令而直接去修改配置文件的话也是可行的操作。

* `git remote`可以查看所有远程名称的列表
	* `-v`或`--verbose`可以查看带有URL所有名称列表
* `add <name> <repo_url>`添加远程地址
	* 使用`git clone`的话，会默认添加一个`origin`作为远程的名称
	* 如果远程库需要更新或者多人协作的话，建议添加安全的`ssh://`的URL
* `rm <name>`删除远程地址
* `rename <old> <new>`更新名称
* `get-url <name>`获取URL信息
* `show <name>`显示详情
* `prune <name>`删除在远程不存在的本地分支
	* `prune origin <name>`删除远程不存在的分支
	* `-n`或`--dry-run`来调试结果


#### fetch

`fetch`会下载远程的信息到本地，而且不会强制把下载的内容合并到本地，所以不会影响到本地原来的状态，属于安全的远程更新。

* `git fetch`更新远程所有的分支
* `git fetch <remote> <branch>`更新特定的远程分支
* `git fetch --all`更新所有的远程项目及分支
* `git fetch --dry-run`调试模式

`fetch`后可以`git checkout remote/branch`查看相关的分支，如果出现`detached HEAD`是正常现象，说明此时的HEAD指针指向的位置不在本地历史中，可以在此创建新分支来建立新的历史，也可以切换到本地其他分支，然后合并进来。

`fetch`后可以通过`git log --oneline master..origin/master`查看本地与master与远程master分支的区别


#### push

`push`将本地的分支内容上传到远程分支，通常是`git push <remote> <branch>`，相当于在远程使用`fast-forward merge`将指针推进到上传的最新进度。如果上传的内容不能满足`fast-forward merge`的话（意思是远程和本地的分支出现分歧），需要首先`git pull`同步到最新的远程进度，再`git push`

* `--force`即强制上传，使得远程分支更新到与本地分支一致，如果不能满足`fast-forward merge`的话，远程某些提交会被覆盖，造成历史丢失
* `--all`上传本地所有分支
* `--tags`上传本地所有tags，而tags是不会通过`git push`默认上传的
* `-u`将新创建的本地分支设置为可追踪的远程分支，比如`git push -u origin <new_feature>`

使用场景：

1. 最常用的是：先`git pull`同步远程分支，再上传`git push`
2. 强行更正最后提交：如果打算修改最后一次已上传的提交，最好在别人更新之前，使用`git commit --amend`修改提交，然后`--force`上传到远程
3. 删除远程分支：
  * 首先删除本地分支`git branch -D <name>`
  * 再删除远程分支`git push origin --delete <name>`或者`git push origin :<name>`


#### pull

`pull`是下载远程分支的内容到本地分支，并且更新本地分支。使用`git pull <remote>`相当于:

1. `git fetch <remote>`
2. `git merge origin/<urrent-branch>`

* `--no-commit`不会产生默认的merge行为的提交
* `--rebase`不会merge，但是会在本地分支历史上添加远程的分支节点（追加拷贝过来的提交）
* `--verbose`打印细节

如果执行下面这句配置，那么`git pull`会默认执行`rebase`替代`merge`

```
git config --global branch.autosetuprebase always
```


### Making a pull request

`Pull Request`(简称`PR`)可以用来给其他人的repo贡献自己的代码，即使你不是他们的内部成员。发起一个`PR`需要设定四个基本信息：

1. 起源仓库（source: 谁发起的，或从哪里发起的）
2. 起源分支
3. 目标仓库（destination: 打算合并进去的仓库）
4. 目标分支

完成一个`PR`的步骤：

1. 在别人公开的仓库中点击`fork`，然后就有了自己的一份拷贝来的远程仓库
2. 通过`git clone`自己的远程仓库到本地，可以建立新的分支来添加功能或修复bugs
3. 把所有改动用`git push`到自己的远程仓库
4. 发起一个`PR`，将自己的这个远程仓库设为`source`，打算合并到别人的仓库作为`destination`
5. 在通过对方代码审核后，可以被合并到指定分支里，结束

步骤的具体细节可以参考[Bitbucket](https://www.atlassian.com/git/tutorials/making-a-pull-request)


### Using branches


#### branch

git分支的创建是一个轻量级的操作，只是生成一个新指针指向当前的位置，展现一个全新的工作区。

* `git branch`默认使用`--list`来查看所有的本地分支
  * `-a`查看所有远程分支
* `git branch <name>`创建一个新分支，但是并没有切换到新分支
  * `-b`创建新分支，并切换到该分支，相当于`git branch <name>`然后`git checkout <name>`
* 删除分支
  * `-d`删除一个分支，如果该分支存在没有合并的提交，则拒绝删除
  * `-D`强制删除一个分支，即使有未合并的提交
  * 删除远程分支的话，参考`push`
* `-m`将当前分支重命名为指定名称


#### checkout <branch>

`checkout`用于在不同版本的目标对象中切换，切换的对象可以是：文件、提交和分支。
`git checkout -b <new_branch> <existing_branch>`用来创建新分支，并切换到该分支，如果没有<existing_branch>就默认为当前分支


#### merge

`merge`作用是将分叉的历史重新合并到一起的过程。合并有两种情况：（以下通过master和feature分支为例子）

1. `Fast Forward Merge`:从master创建了feature分支后，随着feature不断增长，master没有变化，于是两个分支构成一个线性结构。合并的时候只需要将master分支的指针位置移动到feature分支最新的提交位置，就完成了将feature合并回master的过程。
  * `--no-ff`在合并后总是创建一个提交节点，记录合并操作。
2. `3-way Merge`:如果上面的例子中，随着feature不断增长，master自己同样有了新的提交，这样两个分支就分叉了。合并的时候需要创建一个单独的提交，用来作为两个分支的相交点。

在`3-way Merge`的情况下，如果两个分支都修改了同一个文件的同一行位置，合并时候就会终止合并提交而产生冲突。冲突会由特定的的符号来表示：

```
here is some content not affected by the conflict
<<<<<<< master
this is conflicted text from master
=======
this is conflicted text from feature branch
```

通常上部分为接收合并的分支内容，下部分为合并进来的分支内容。解决冲突后，就可以继续进行未完成的合并提交。


### Comparing workflows

工作流的几种类型：

* `Centralized`：像svn一样，所有人围绕一个远程的中心仓库来协作开发，适合小团队开发
* `Feature Branch`：根据不同功能建立相应的分支，保持主干分支的稳定（不包含正在开发中的代码）
* `Gitflow`：利用git的特性和实际开发的生产环境进行严格划分的工作流，包含`master, develop, release, hotfix`等专用分支
* `Forking`：从官方项目的远程仓库那里，克隆一份作为自己项目的远程仓库，可以不受官方限制而修改源码，也可以和官方协作开发，常用在开源项目中
	* 在fork工作流中，会存在两个远程仓库，惯例上命名为：官方远程仓库`upstream`和自己fork来的远程仓库`origin`
	* 在`git clone`自己的远程仓库时候会自动创建origin名称，而官方仓库名需要自己添加`git remote add upstream <official_codebase>`
	* 同步官方远程最新的代码`git fetch upstream`或者`git pull upstream master`

**merge vs. rebase**

分支从远程更新也可以用rebase的形式：

```
git pull --rebase origin master
```

如果出现冲突，那么会终止当前的rebase操作，通过`git status`查看冲突文件，解决后可以继续rebase

```
git add <some_files>
git rebase --continue
```

之后git会继续在rebase过程中查看下一个提交是否构成冲突。如果希望撤回rebase操作的话，可以

```
git rebase --abort
```


### Other git commands


#### grep

搜索工作区的改动内容，比如`git grep 'hello'`


#### show

显示信息，比如提交、标签等等


## Advanced Tips


### Merging vs. Rebasing

这两个命令其实都是为了将分岔的工作流统一起来的方法，只是实现方式不同而已。`merge`是一种不会破坏历史线的安全方式，但是缺点是多次的合并会让不同的分支之间出现多次的穿插记录；而`rebase`是通过修改历史来创造出一个干净的线性工作流，方便代码审核与历史的可读性。

在合并或同步工作流时，如果害怕出错的话，完全可以使用保守的`merge`方式；而其他某些情况下是`rebase`施展身手的时刻，比如：**在本地feature分支上重新整理之前的提交历史，构造一个更简洁清晰的历史线**。首先用`merge-base`命令找到开启分支/分岔点，然后通过交互式的`rebase`来重头整理这个feature分支的每个提交。

```
git merge-base feature master # 返回一个分岔的commit_id
git rebase -i <commit_id>
```

但是使用`rebase`要遵守一条黄金定律，就是`rebase`不能用在公共分支上！因为其修改历史记录的特性会影响到其他协作同伴的工作流。

不过有个情况可行，比如我和Mary两个人都在一个公共的feature分支里工作，我仍然可以把`Mary/feature`远程分支`fetch`下来，然后将自己的改动`rebase`到Mary的最新成果上，因为我没有修改Mary的工作历史，所以不会出问题。

如果把自己的feature分支开启了`Pull Request`，让其他团队成员来代码审核，那么之后的改动就不要再`rebase`了，因为使用了`PR`后，大家都可以看到你的提交，意味着这个feature分支已经是公共分支了，别人也许会修改它。当该分支审核通过后，你仍然可以用`rebase`来让feature分支更新到master最新的节点，让feature保持线性历史，只要别修改master的历史就好。

假如对`rebase`操作没有足够信心的话，可以创建一个临时分支进行`rebase`实验，即使出错也可以`checkout`重来。


### Resetting, checking out and reverting

这里对比了几种回退历史的方法：

| Command      | Scope        | Common use cases                                                     |
| ------------ | ------------ | -------------------------------------------------------------------- |
| git reset    | Commit-level | Discard commits in a private branch or throw away uncommited changes |
| git reset    | File-level   | Unstage a file                                                       |
| git checkout | Commit-level | Switch between branches or inspect old snapshots                     |
| git checkout | File-level   | Discard changes in the working directory                             |
| git revert   | Commit-level | Undo commits in a public branch                                      |
| git revert   | File-level   | (N/A)                                                                |

#### 回退提交历史

在回退提交历史的操作里，`reset`和`checkout`区别是：`reset`是将分支的末端位置设置成以前某个历史节点，这样会导致该节点之后的提交被遗弃到了分支的外面（过一段时间后会被垃圾收集器清理掉）；而`checkout`会保留分支的末端位置，只是移动当前的HEAD指针指向以前某个历史节点，用于查看当时的项目状态。`checkout`切换分支也是将HEAD指针移动到不同分支的末端位置。相对于他们来说，`revert`是通过增加新的历史节点来实现重置以前某个提交的改动。

#### 撤回文件

`reset`和`checkout`也可以分别重置某个文件到之前的历史状态，而且不会改动历史线。

* `git reset <commid_id> <file_path>`会把指定文件在过去某个历史时刻的状态，放入到`staging`区
* `git checkout <commid_id> <file_path>`会把指定文件在过去某个历史时刻的状态，改回到`working`区

`git reset HEAD~2 foo.py`会将该文件的状态返回到HEAD前两个提交那里，并且将当时的状态摆设到`staging`区域，等待用户提交；而且将撤销前的现状摆设到`working`区，保留撤销前的现场，现在给用户两个选择：

1. `git commit`，一旦直接提交的话，新增的提交中该文件就变成了当时的样子
2. `git add`，执行以后，文件就跟撤销前一样，没有变化

`git checkout HEAD~2 foo.py`会将文件状态恢复到指定时候的样子，然后将恢复操作摆设到`staging`区，一旦提交的话，新增的提交里该文件就成了过去的样子。

所以总结回退文件的话，通过`reset`不能直接看到文件的变化，因为变化在`staging`区，需要`git diff`可以对比从某时刻到现在的变化；而`checkout`可以直观地看到文件某个历史时刻的状态。前者看变化，后者看状态。


### Advanced git log

### Git hook

### Refs and Reflog

### Git LFS

## 参考

[atlassian git tutorial](https://www.atlassian.com/git/tutorials)


