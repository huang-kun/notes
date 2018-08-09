
## 在macOS切换多个版本的python

`macOS`系统自带一个`2.7`版本的`python`作为稳定版本。由于我需要学习`python3`的话，就得自己下载了。后来使用`brew install python3`下载了当前最新的`3.7.0`版本。但是由于某些原因，我仍需要使用`3.6.5`的版本，怎么才能用brew回退到指定的python版本呢？

我在网上找到了[解决方案](https://stackoverflow.com/questions/51125013/how-can-i-install-a-previous-version-of-python-3-in-macos-using-homebrew)，brew可以通过指定包地址来安装相应的程序，比如这里：

```
brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/<id>/Formula/python.rb
```

将这个链接里的`<id>`替换成对应版本的id即可，我在[这个提交历史里](https://github.com/Homebrew/homebrew-core/commits/master/Formula/python.rb)找到`python 3.6.5_1`版本时候更新的提交，点击去获取相应的id信息，然后下载安装。

下载安装后，目前在我的`/usr/local/Cellar/python`目录下就保存了两个python的版本目录：`3.6.5_1`和`3.7.0`，使用以下命令就可以切换python3的版本了：

```
brew switch python 3.6.5_1
```

接着需要解决`brew link`的问题，因为之前已经安装过相应的python3程序（无论是否来自brew的程序），可以通过`brew link --overwrite python`覆盖之前安装程序的设置。然后使用`python3 --version`发现已经成功切换到3.6.5版本。

打算切回最新版本的话，按照同样的方式把3.6.5_1换成3.7.0就OK。


