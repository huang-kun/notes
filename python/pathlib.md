# pathlib速查表

使用

```
from pathlib import Path

Path.cwd()      # 当前路径 PosixPath('/Users/jack/...') 或者 WindowsPath('C:/...')
Path.home()     # 用户主目录
```

添加路径

```
Path.home() / 'Dev'     # PosixPath('/Users/jack/Dev')
Path.home().joinpath('Dev') 
```

读写文件

```

```