
### 操作步骤
1. 拥有一个github.com的账号
2. 本机打开terminal, 进行如下操作
```sh
# 建立公秘钥
ssh-keygen -t rsa -C "这里换成你的邮箱@example.com"
# 这个命令可以直接copy公钥
pbcopy < ~/.ssh/id_rsa.pub
```
3. 更新这个秘钥到github
4. 本机terminal, 进行如下操作
```sh
git clone git@github.com:lornally/algorith2rich.git
```
### 无法搜索
搜索 git@github.com:lornally/algorith2rich.git, 现实没有结果
- 搜索这个: lornally/algorith2rich

### 链接的区别
https, ssh和github cli的区别
- https是为了防止封锁, https协议是不可能被封锁的, 但是很挫, 不要用.
- ssh是正解, 正常用的模式
- cli是github自己的command line interface, 新的命令行, 没用过

### git pull报错
- 看一下是否在目录下


### add和commit的区别
- 别急, 有个ppt解决这些问题