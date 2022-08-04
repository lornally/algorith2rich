### 设置

```sh
code ~/.gitconfig
# 修改config
[user]
	email = catalina@17mbp.com # 你的邮箱, 不需要真实性, 但是要能够做区分
	name = m的17寸mbp # 你的名字, 同上
[core]
  quotepath =false # 解决中文路径问题
  editor = mate -w # 设置默认编辑器, 注意此处一定要-w, 不然shell不等待编辑器返回, 最近在才开始有这个问题.
[pull]
	rebase = true # 这样pl就是 fetch + rebase
	
# 设置editor可能会不生效, 检查下mate的设置里面的terminal项目重新安装一下, 然后用命令行:
 git config --global core.editor mate
```



### 一个最佳实践的模拟最长流程

```sh
git init # 当前目录开始被git版本化管理

git remote add # = gra
gra remotename git@github.com:lornally/oh-my-mac.git # 把一个git远程仓库加为源, 并且这个仓库命名为remotename
gr -v # 列出所有源

# 设置默认源
git push # = gp
gp -u remotename  #设置默认远程源
gp -u remotename main #设置默认分支,
# 如果main被保护, 上面这句就要替换为下面的方法.
gb --set-upstream-to=remotename/main main #这个如此复杂, 可以直接去.git目录改config
gr remove xxx # 删除一个远程源

# 更新并且变基
git fetch # =gf
git rebase # =grb
git pull # =gl
# 默认的gl是merge, 两个方法可以改为rebase: 
git pull --rebase # gup 或者 gupv, 用这个可以不用改下面的设置
# 需要到git的config里面修改, 这个修改可以去改全局配置, 例如: ~/.gitconfig
[pull]
rebase = true
# 注意此处严重不推荐下面这种配置, 因为工作分支, 随时可能干掉, 并且工作分支的推拉不一致, 拉主要是拉main, 推主要是推自己的对应远程
[branch "dev"]
    remote = origin
    merge = refs/heads/develop

# 不小心在错误的分支做了开发
# 需要紧急拉取远端的版本
# 此时都需要暂存stash
git stash push # gsta 将暂存入栈, 做切分支或者rebase之前, 可以做多次. 每次都入栈.
git stash pop # gstp 将暂存出栈, 做完rebase操作或者切分支操作后
git stash list # gstl		
git stash show --text # gsts  查看差异

# 拉分支进行开发
git branch #gb #列出所有分支
gcb xxx #新建xxx分支
gco xxx #切换到xxx分支

# 编辑类操作
git add -all # gaa 这个可以做多次, 每次都是把修改提到跟踪区.
git diff --staged # gd --staged 查看差异
git diff #    缩写: gd 查看差异 同上

git commit -v # gc
git commit -a -m # gcam 这个也可以做多次, 每次都是提到本地版本中. 这个一般不是最终提交, 所以命名最好有自己的规律, 避免影响下面的合并操作.
grb -i @~3 # 合并3次提交, 按照咱们的开发要求, 一个pr是一个rebase的commit才可以, 因此需要合并提交.

# 追加一次提交
git commit -v --amend # gc!
git commit -v -a --no-edit --amend # gcan!


# 变基及远程操作
gl gitee main #把gitee源的分支main拉到本地的当前分支
gp ooo xxx #本地xxx推到远程ooo

grb main #把dev分支的内容合并回来. 这个操作要慎重, pr之后最好删除分支(因为可能在网站进行了自动合并).
gb -d dev # 删除本地分支dev
git push origin --delete BranchName #删除远程origin的分支BranchName
git fetch -p #清除远程不存在的本地的远程分支
gr prune gittee # 清除远程源gittee上的不存在分支



# 查看, 编辑类操作需要很多查看命令
# 查看log
git log --graph --color #glgg
git log --graph --decorate --all #glgga
git log --graph --max-count=10 #glgm
git log --oneline --decorate --color --graph #glog
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit #glol
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --all #glola
gloga # 这个也是可以的 
# 查看差异
1. 目前暂存stash中的修改：
git stash show --text # gsts  查看差异
2. 尚未缓存add的改动：
git diff #    缩写: gd
3. 查看已缓存add的改动： 
git diff —-cached # 缩写: gdca
git diff --staged # gd --staged
4. 查看已缓存的与未缓存的所有改动：
git diff HEAD # gd @
5. 显示摘要而非整个 gds：
git diff --stat # gd --stat
6. 可视化
git diff-tree --no-commit-id --name-only -r # gdt
7. 精简为文字差异
git diff --word-diff # gdw
8. 查看版本之间的差异
git diff HEAD~2
# 最简洁的写法, 这里面 ~=^, @=HEAD
gd @^
gd @~
gd @~3
gd commit_id
9. 用show命令
git show --pretty=short --show-signature # gsps


```

#### fork流程(triangular模式)

```sh
gcb m # 拉新分支, 这个必须命令行, 否则配置文件无效
# 最终配置文件
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
	ignorecase = true
	precomposeunicode = true
[remote "origin"]
	url = git@github.com:bunny-nest/tianyandesign.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main
[remote "team"]
	url = git@github.com:bunny-nest/tianyandesign.git
	fetch = +refs/heads/*:refs/remotes/team/*
[remote "myfork"]
	url = git@github.com:lornally/teamdoc.git
	fetch = +refs/heads/*:refs/remotes/myfork/*

[remote]
	pushDefault = myfork

[branch "m"]
	remote = team # 找到当前的工作分支, 然后, 把她的远程源设为要fetch的地址
	merge = refs/heads/main # 这里要指定远程fetch的分支
# 建议doc仓库设计pull用rebase模式
```



```sh
# 本地添加基础的远程源, 未来要pr到的原始源, pull也从这里, 源命名为team
gra team git@github.com:bunny-nest/tianyandesign.git
# 本地添加自己的fork仓库, 未来要push的源, 源命名为myfork
gra myfork git@github.com:lornally/teamdoc.git
# 查看一下远程源有哪些, 此时可以看到所有的提交
git remote -v #gr -v
# 从team源拉取, 每次push之前都要先拉取, 避免冲突
git pull team #gl team
# 向myfork提交, 注意如果不指定分支, 提交的是当前分支
git push myfork #gp myfork 
# 此时登录github官网, 不论是team还是myfork如果有权限都可以提pr, 如果team没权限, 那么就在myfork里面发起pr


### 设置 -------------------------------------------------
# 设置默认push源
# 原本的方法, 并不适用, 因为我们的push和pull要使用不同的源. gp -u myfork # 不要用这一行
git config remote.pushDefault myfork # 等于在config增加了一行配置
# 实质上是在操作配置文件, 我们直接修改文件是最方便的..............
# .git/config # 这个配置文件
[remote]
	pushDefault = myfork
	
	
# 设置默认拉取源
[branch "m"]
	remote = team # 找到当前的工作分支, 然后, 把她的远程源设为要fetch的地址
	merge = refs/heads/main # 这里要指定远程fetch的分支
# 建议doc仓库设计pull用rebase模式
[pull]
	rebase = true

### 设置之后的操作会比较简化---------------------------------0
# add, commit, rebase合并本地commit为一个之后
git pull # gl 拉取
# 处理冲突之后
git push # gp 推送
# 此时可以登录github提交PR了
```

- 注意
  - 原始库被删掉, fork库也会消失.
  - github如果不是fork, 不能拉取
  - 虽然不能拉取, 但是, 可以管理员硬推.

###### 找回

```sh
# 找回孤儿commit
git reflog 
gcb xxx 342w242v # 把需要恢复的commit 342w242v 恢复到分支xxx
# 找回最后一次add,  todo
```

###### 对于一个提交后悔了

```
git reset --soft c5a503d
```



###### 典型错误

- 左脚踩右脚, 要么是本地合并rebase跨越了远程, 要么是远程发生了rebase合并.

```sh
# 本地合并跨域远程的问题
gco a2560a3 #取回之前的最后一个commit
g switch -c xxx #gswc 在这个commit上, 新建一个xxx分支
# 此时, gloga可以看到, 提交是正确的. 然后正确的grb, 然后gl, 因为没有默认的源和分支, 系统会要求指定
gb -D m #删除原本的m分支
gb -m xxx m # 用新建的xxx分支重命名为m分支
# 此时要查看一下.git/config 看看设置是否正确, 大概率m分支原本的设置不见了. 正常使用其实没有影响, 不过如果是fork流程导致的三角模式, 那么需要参考上面的fork流程
```

- gitignore没配对

```sh
# 改的时候很神奇
target          //这个不生效  # 原因是//做注释, 应该是#号注释
unpackage    //这个也不生效
*/target/
*/unpackage/

# 改好之后
git rm --cached  -r .
gaa
gcam
# 这个世界清净了
gp #推到服务端

```

