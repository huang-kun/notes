CocoaPods版本升级：

1、更新gem：sudo gem update --system
2、删除gem源：gem sources --remove https://ruby.taobao.org/
3、修改gem源：gem sources -a https://gems.ruby-china.org
4、查看gem源是否是最新的：gem sources -l
5、升级cocoapods：sudo gem install -n /usr/local/bin cocoapods
6、查看升级后的cocoapods版本：pod --version

参考[cocoapods的升级更新](https://blog.csdn.net/potato512/article/details/62235282)

