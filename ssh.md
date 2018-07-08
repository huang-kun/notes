# SSH

SSH是Secure Shell的缩写。使用SSH来进行远程和本地之间的文件上传或者下载，就省去了需要用户名和密码的输入验证，不仅安全，操作也更便捷。

ssh的原理是给自己的账户分别创建公钥(public key)和私钥(private key)，然后将私钥保存在本地，将公钥上传到远程，之后进行ssh服务器连接的话就需要通过密钥验证。由于别人不会拥有你自己的私钥，因此就避免了所谓的“中间人”攻击。

* 创建ssh钥匙对`ssh-keygen`
* 拷贝公钥`cat ~/.ssh/id_rsa.pub | pbcopy`

## 参考

* [SSH Keys](https://confluence.atlassian.com/bitbucket/ssh-keys-935365775.html)