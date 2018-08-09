# pathlib笔记

出自[Python3的pathlib模块：驯服文件系统](https://mp.weixin.qq.com/s/LDoZ9wng9Vi1ADmLu84fsw)

使用

```
from pathlib import Path

Path.cwd()      # 当前路径 PosixPath('/Users/jack/...') 或者 WindowsPath('C:/...')
Path.home()     # 用户主目录
```

路径拼接符

```
Path.home() / 'Dev'     # PosixPath('/Users/jack/Dev') 要求至少又一个Path对象才可以使用'/'连接符号，如果连接的部分带有根目录的`/`，那么之前的根目录会被替代！
Path.home().joinpath('Dev') 
```

读写文件

既可以像`open`函数一样使用`with path.open(mode='r') as f:`，还可以使用简单函数比如`read_text()`,`read_bytes()`,`write_text()`,`write_bytes()`,这些方法自己处理文件打开和关闭。

路径

```
path = Path() # 当前路径
path.resolve() # 完整路径
```

| 属性   | 解释                                             |
| ------ | ------------------------------------------------ |
| name   | 没有任何目录的文件名                             |
| parent | 包含该文件的目录，或者如果path是目录，则是父目录 |
| stem   | 文件名不带后缀                                   |
| suffix | 文件扩展名                                       |
| anchor | 目录之前的路径部分                               |

| 方法          | 解释                                            |
| ------------- | ----------------------------------------------- |
| exists()      | 是否存在                                        |
| replace()     | 覆盖、替换                                      |
| with_name()   | 新的名字组成的path                              |
| with_suffix() | 新后缀组成的path，必须有'.'                     |
| iterdir()     | 子目录生成器                                    |
| glob()        | 子目录匹配生成器，必填参数pattern是匹配模式     |
| rglob()       | 递归子目录匹配生成器，必填参数pattern是匹配模式 |
| stat()        | 文件底层信息                                    |
| rmdir()       | 删除目录                                        |
| unlink()      | 删除文件                                        |