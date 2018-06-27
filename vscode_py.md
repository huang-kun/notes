
# 使用Visual Studio Code开发Python

Visual Studio Code（简称vscode）是微软开源的一个IDE，目前可以支持多种语言的项目开发。我目前学习python，所以在IDE方面，它是除了`PyCharm`以外的最佳选择了。

* 安装版本：社区版1.21.0
* 运行系统：macOS High Sierra
* 开发语言：python 3.6.5


## 配置python环境

最初打开vscode的时候，就好像是一个空壳子，只负责打开文件或者文件夹，没有像PyCharm那样集成了Python的环境，上手就工作。但是vscode允许用户为自己喜欢的程序语言搭建工作环境，比如javascript, php等等，给我的感觉反而更灵活一些。我在这里总结一下vscode官方文档里关于搭建python环境的过程。


#### 使用vscode前，先创建项目环境

我在我的macbook里已经安装好了python3.6版本，我打算实现官方给的数学绘制图的demo，这里需要安装matplotlib和numpy两个第三方的库。为了做到python项目之间安全的环境隔离，需要使用到`virtualenv`

1. 开启terminal，如果没有`virtualenv`的话，安装虚拟环境`pip3 install virtualenv`
2. 创建项目路径`mkdir MathLab`，进入项目`cd MathLab`
3. 创建隔离环境`virtualenv --no-site-packages venv`，后面的参数意思是创建一个没有任何的第三方库的环境
4. 进入隔离环境`source venv/bin/activate`
	* 这时候命令行提示符出现`(venv)`的前缀，表示当前的环境是该项目的隔离环境，不会受到系统python环境的干扰
	* 在这里输入`which python3`可以看到这里运行的python解释器是该环境下的解释器
5. 在隔离环境里安装该项目使用的第三方库，比如这里需要matplotlib和numpy
	* `pip3 install matplotlib`
	* `pip3 install numpy`
6. 通过命令`deactivate`可以退出隔离环境


#### 配置vscode项目

运行vscode，打开`MathLab`文件夹就相当于进入了项目开发环境。这里首先需要确定的是，该项目使用的是哪个python解释器。在vscode最下方有一条蓝色的提示条，显示了当前的解释器。如果是`Python 3.6.5 (virtualenv)`，说明使用的是我刚才创建的隔离环境中的python解释器；如果是`Python 2.7`这样的话，说明是mac OS X自带的系统python解释器了。

* 根据需求，也可以在vscode中切换解释器
	* `⇧⌘P`，出现一个带有`>`的命令框
	* 在`>`后面输入`select interpreter`，回车后就可以选择解释器
* 如果没有合适的解释器（比如用隔离环境）的话，也可以给vscode添加解释器
	* 找到项目目录下的`.vscode/settings.json`文件，用vscode打开
	* 在用户自定义区域里定义一个`"python.pythonPath": "./venv/bin/python3.6"`
	* 如果安装了隔离环境的话，就可以使用隔离环境中的python解释器了


#### 运行和调试代码

配置好了python环境，终于可以写代码了。创建一个`hello.py`的文件，写下：

```
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np 

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
```

这时候，还要配置一下vscode的代码运行和调试环境。点击左侧的“Bug图标”，然后在左上角的调试栏中点击“设置图标”，在项目中会出现一个`.vscode/launch.json`文件，内容大概是这样的：

```
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}"
        },
        ...
}
```

按照这个配置，切换到`hello.py`，点击左上角的绿色“运行”箭头，解释器就会执行当前的`hello.py`文件。如果需要断点调试的话，可以把鼠标移到相应代码行左侧，会出现红点提示，点击后就可以激活断点。再次运行就可以让程序停止在那里，然后可以点击step in, step over等调试按钮。

但是在vscode运行后，发现没有什么结果。于是我使用命令行，进入到`(venv)`环境下运行`hello.py`，结果看到了绘制的曲线图。


## 开启REPL环境

使用REPL环境可以在交互式的命令行中开发python，在vscode使用`⇧⌘P`开启命令输入框，输入`> start repl`，回车开启REPL环境。


## lint

程序语法的静态检查对于开发来说还是相当重要的，我个人可不希望写完一堆代码后，一拿去执行才发现各种语法错误编译不过。vscode会自带Pylint作为静态检查器。每次保存文件时，如果有错误，就会提示。当然也有可能因为配置了新的隔离环境而导致了没有lint检查器的情况，于是就需要自己安装，方法如下：

1. 在vscode终端，通过`source venv/bin/activate`进入隔离环境
2. 使用`pip3 install pylint`下载检查器
3. 快捷键`⇧⌘P`开启命令框，使用`>select linter`命令，选择`pylint`
4. 编辑python文件，保存，如果有错误的话出现提示，说明安装成功


## 常用快捷键

* 新建文件`⌘N`
* 查找`⌘F`，替换`⌥⌘F`
* 命令选择框`⇧⌘P`
* 切换标签tab
	* 向左`⇧⌘[`
	* 向右`⇧⌘]`

* 光标移动
	* 移到行首`⌘←`
	* 移到行尾`⌘→`
* 光标高亮
	* 高亮右侧至行尾`⇧⌘→`
	* 高亮左侧至行首`⇧⌘←`
* 代码缩进
	* 向右缩进`⇥`（或`⌘]`）
	* 向左缩进`⇧⇥`（或`⌘[`）


## 快速创建flask项目

1. `mkdir HelloFlask` # 创建项目
2. `cd HelloFlask` # 进入项目
3. `python3 -m venv env` # 创建隔离环境
4. `code .` # 用code命令直接打开vscode，安装需要code命令，方法是`>shell command: install code command in path`
5. `>select interpreter` # 选择 ./env/bin/python 即隔离环境下的解释器
6. `>create terminal` # 直接进入(venv)命令行
7. `pip3 install flask` # 安装flask框架
8. 创建一个`app.py`，写好初始化代码

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'
```

* 终端运行：在终端通过`(venv) python3 -m flask run`运行程序，还可以带参数`--host=0.0.0.0 --port=80`
* 调试运行：选择vscode的Bug图标 -> 调试设置图标 -> 生成launch.json -> 选择"Python: Flask (0.11.x or later)" -> 点击箭头运行


## 参考

	* [Visual Studio Code Docs: Getting Started with Python](https://code.visualstudio.com/docs/python/python-tutorial)