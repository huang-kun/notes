# BeautifulSoup4速查表

## 安装

```
pip3 install beautifulsoup4
pip3 install lxml # 安装一个第三方的快速解析器
```

## 创建soup

```
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')
print(soup.prettify())
```


## Tag对象

```
soup.head # <head><title>The Dormouse's story</title></head>
soup.head.title # <title>The Dormouse's story</title>

soup.title # <title>The Dormouse's story</title>
soup.title.name # u'title'
soup.title.string # u'The Dormouse's story' 这不是str类型，是NavigableString类型
soup.title.parent.name # u'head'
```

### tag属性

tag的属性可以被添加,删除或修改.
tag的属性操作方法**与字典一样**

```
# 单值属性 <p class="title"><b>The Dormouse's story</b></p>
soup.p.attrs # { u'class' : u'title' }
soup.p['class'] # u'title'

# 多值属性 <p class="body strikeout"></p>
soup.p['class'] # ["body", "strikeout"]
```

### tag层级

```
# 获取孩子节点 
# <div><h2>hello</h2><p>world</p></div>
# 层级结构是：
# - div (Tag)
#   - h2 (Tag)
#     - hello (NavigableString)
#   - p (Tag)
#     - world (NavigableString)

# contents获取孩子列表
soup.div.contents # [<h2>hello</h2>, <p>world</p>]
soup.div.h2.contents # ['hello']

# children生成器
list(soup.div.children) # [<h2>hello</h2>, <p>world</p>]
for child in soup.div.children:
    print(child)
    # <h2>hello</h2>
    # <p>world</p>

# descendants可以对所有tag的子孙节点进行递归循环
list(soup.div.descendants) # [<h2>hello</h2>, 'hello', <p>world</p>, 'world']
```

其他tag关系还包括:

* 父级：
    * `.parent`上级节点
    * `.parents`生成器，递归得到元素的所有父辈节点
* 兄弟：
    * `next_sibling`, `previous_sibling` 这里有坑，比如`,\n`都可能是下一个或上一个节点
    * `next_siblings`, `previous_siblings`
* 前进后退：
    * `next_element`, `previous_element`
    * `next_elements`, `previous_elements`


### tag.string

一定需要考虑到tag.string的值可能是None的情况！
e.g. `<div><h2>hello</h2><p>world \n</p></div>`

```
# 如果tag只有一个 NavigableString 类型子节点，可以用.string获取
soup.div.h2.string # 'hello' (NavigableString)
soup.div.string # None (NoneType)

# 如果tag包含多个 NavigableString 类型子节点，可以用.strings, .stripped_strings
list(soup.strings) # ['hello', 'world \n']
list(soup.stripped_strings) # ['hello', 'world']
```


## 搜索

### 搜索标签

```
# 搜索所有的<a>标签
soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# 搜索多个标签
# 下面代码找到文档中所有<a>标签和<b>标签
soup.find_all(["a", "b"])

# 返回所有的标签，不包括字符串节点
soup.find_all(True)

# 特殊标签筛选，传入函数作为参数
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

soup.find_all(has_class_but_no_id)
```

### 搜索id

```
soup.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
```

### 搜索css的class

```
soup.find('p', class_='item')
```

### 正则表达式

```
# 下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到
import re
soup.find_all(re.compile("^b")):

# 其他参数也可以用正则表达式
soup.find_all(id=re.compile("^\d+$"))
```

### 其他参数：

* text: 搜索字符串内容
* limit: 限制结果数量
* recursive: True表示可以递归查找子孙节点（默认），False表示只返回子节点

### 信息提取

```
# 从文档中找到所有<a>标签的链接:
for link in soup.find_all('a'):
    print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie
```

## 参考

[Beautiful Soup 4.2.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

