这是一个markdown文件, 可以用任何文本处理器打开, 记事本就可以.

## mac的购买
-  购买渠道
    -  如果一定要新机, 那么可以学生价/教师价
    -  苹果官网有官翻机, 物美价廉
    -  也可以考虑买二手, 尤其是在保的, 有问题, 可以找苹果保修
-  购买配置
    -  cpu无所谓, 机型也无所谓, air/pro/mini/book等等都差不多
    -  内存最关键, 一定要加到满, 最严重影响速度的硬件
    -  硬盘量力而为, 苹果的价格比较贵, 但是也不能扩展, 都是焊死的并且还有验证芯片, 所以其实也建议买大一点的, 但是真的贵
-  购买笔记本的特别建议
    -  建议优先考虑移动性, 买尺寸最小的
    -  因为, 笔记本的屏幕一般用处不大, 
    -  如果日常工作或者开发一定要配外接显示器.
    -  如果旅行/出差/带回家, 那么重量和尺寸就非常关键了, 太重的机器会引起肩周炎.
    -  因为sony毕业了, 所以mac没有11/12寸了, 目前最小且配置最好是13air, 屏幕尺寸比pro大, 分量比pro轻, 比pro薄, 性能至少等同于pro, 建议入手

mac的使用
-  git@github.com:lornally/oh-my-mac.git
-  isuyu.cn
-  winry有一个mac使用的分享


## git基操
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
- 可以, 腾讯会议, 看群公告

### 无法搜索
> 症状: 在github.com里面搜索 git@github.com:lornally/algorith2rich.git, 显示没有结果
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
  - win的命令行尽量避免使用， 直接使用web， 比如GitHub.com, 如果强行用win命令行会碰到各种问题, 例如中文问题, 命令不兼容, 库不支持...
  - win上有最好的(没有之一)编辑器nodepad++, 这个是远超vscode/sublime/textmate, 易用性好于vi/emacs
3. 不过吧， 如果把时间折算成本， 还是买个二手或者官翻mac(苹果官网就有)吧, 价格四千以内, 这玩意的收益可比手机大太多了

### windows无法克隆含有中文路径的项目怎么处理？
1. 直接在github.com网页上操作
2. Windows安装Ubuntu子系统操作

### notebook
补充说明 notebook可以分段运行，但一个文件内，运行时是有关联关系的，前一次运行的框框定义的a在后一次运行的框框中，可以直接使用，代表含义相同

