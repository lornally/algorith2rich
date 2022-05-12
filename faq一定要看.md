
## 基操
> 这个基操很重要, 所有的文档资料代码(包括入门文档), 大家尽量看git上面的, 群文件不会更新和维护, 也不会同步最新版, 最新的版本只可能在git上面
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

## 疑问--------

### 可否线上会议
- 可以, 腾讯会议咱们试试

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


### 不用mac可以吗?
> 结论: 或许是可以的, 但是并不经济, 因此并不推荐这个方案
0. 如果使用linux也是可以的, 非常不建议使用win, 很浪费时间
1. 直接装anaconda, ltm版本
2. 如果使用win, 有两个特别注意
  - win的命令行尽量避免使用， 直接使用web， 比如GitHub.com
  - win上有最好的(没有之一)编辑器nodepad++, 这个是远超vscode/sublime/textmate, 易用性好于vi/emacs
3. 不过吧， 如果把时间折算成本， 还是买个二手或者官翻mac(苹果官网就有)吧, 价格四千以内, 这玩意的收益可比手机大太多了

### windows无法克隆含有中文路径的项目怎么处理？
1. 直接在github.com网页上操作
2. Windows安装Ubuntu子系统操作