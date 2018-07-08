
## Pycharm使用系统级解释器

1. 在命令行中找到python3程序的路径：`which python3`，把地址拷贝下来
2. 打开Pycharm项目，菜单中选择`File -> Default Settings...`
3. 选择`Project Interpreter`，点击设置icon中的`Add...`
4. 选择`System Interpreter`，点击更多icon后，将拷贝的地址粘贴到那里，选择列表中的python3程序
5. 保存设置，回到项目，菜单中选择`Run -> Edit Configurations...`，在左侧选择当前工作中的python文件，在后边的`Python Interpreter`选项中选择新添加的系统python3程序
6. 于是在命令行中使用`pip3 install xxx`下载的工具，就可以直接使用到Pycharm项目中了
