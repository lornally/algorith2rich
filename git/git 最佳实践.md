# 最佳实践：Git 篇

## 绝对禁止项目

```bash
git push -f
```

多人项目时来一下，这酸爽，谁做谁知道

茂弘特别叮嘱：做这件事的人，直接开除。


## 最佳实践

### 拉取远程仓库代码

在拉取远程分支后，使用 rebase 合并，这样操作可以使提交记录保持清爽整洁

good 👍

```bash
git fetch
git rebase

# or

git pull --rebase
```

bad 👎

```bash
git fetch
git merge

# or

git pull
```

### 解决 rebase 时产生的冲突

当 rebase 发生冲突时，git 会停止 rebase 并让你去解决冲突，解决完之后不能直接 commit，而是应该用 continue 参数继续执行 rebase

good 👍

```bash
# 解决冲突之后
# 如果是合并代码时产生的冲突，需要把修改的文件放入暂存区
git add <冲突的文件>
git rebase --continue

# or

# 不解决冲突，还原回 rebase 之前的状态
git rebase --abort
```

bad 👎

```bash
# 解决冲突之后千万不要做一下操作
git add <冲突的文件>
git commit 
# or
git rebase
# 什么都不做
```

### 合并多个 commit

其实你并不需要那么多 commit，大量琐碎的 commit 只会导致提交记录的混乱

good 👍

```bash
$ git log --oneline --graph
* 6552ad8 (HEAD -> test) docs: commit 3
* ecc83f1 docs: commit 2
* d010d09 docs: commit 1

# 指定想要合并的commit数量
$ git rebase -i HEAD~3
```

之后会看到如下界面，具体配置含义可查看注释

```bash
pick d010d09 docs: commit 1
pick ecc83f1 docs: commit 2
pick 6552ad8 docs: commit 3

# Rebase e3cf73d..6552ad8 onto e3cf73d (3 commands)
#
# Commands:
# p, pick <commit> = use commit
# r, reword <commit> = use commit, but edit the commit message
# e, edit <commit> = use commit, but stop for amending
# s, squash <commit> = use commit, but meld into previous commit
# f, fixup <commit> = like "squash", but discard this commit's log message
# x, exec <command> = run command (the rest of the line) 
```

假设我们需要把后两次提交合并到第一次提交上，
那根据需求把文档编辑如下：

```bash
pick d010d09 docs: commit 1
s ecc83f1 docs: commit 2
s 6552ad8 docs: commit 3
```

保存后更新 commit message 即可完成操作

```bash
$ git log --oneline --graph
ee6f458 (HEAD -> test) docs: commit all
```

bad 👎

```bash
# 不合并直接推送
git commit -m "new commit"
git commit -m "new commit"
git commit -m "new commit"
git push 
```



## 原则

### 用branch, 避免直接在master/main做修改

- 善用branch可以省去很多烦恼
- 禁止在master/main进行开发, 除非走fork分库流程
- 因为提交可能不被接受.

### 所有的commit都是fast forward

- 使用rebase, 而不是merge, 避免merge传递.
- 都是fast forward, 可以整理版本为线性, 方便各种回退/pick/cherry/拆库等等操作.

### 一件事有且只有一个commit

###### 例如: 正在dev开发代码的过程中, 发现自己需要修改配置.

1. 从master拉一个分支.
2. 修改配置.
3. 发起pr.

###### 例如: 开发了一整天, 修复了一个大bug, 改了代码, 文档, 配置...

1. 因为干了一整天, 很可能有多个commit, 因此要做一次commit合并(同样使用rebase命令). 
   - 注意: 这一步要先做, 因为如果冲突, 那么多个commit很可能要多次手工处理.
2. 此时很可能别人已经做了提交, 因此, 要先做针对origin/master的rebase, 把提交整理为ff(fast forward), 避免提交merge.
3. 发起一次完美的pr
4. 再次强调, 合并commit为一个很重要, 因为git网站(比如码云)有个自动合并, 所以多个commit会导致本地这个分支就不能再使用了.

### 复合型操作都是坑

- 修改远程源
  - remove + add ok
  - rename + add ok
  - seturl 这个就出问题了
- 拉取变基
  - gf +grb ok
  - gl直接弄, 这是坑
- 推送远程
  - 必须建分支, 因为推送有对应分支关系, git并不保证推送当前工作分支., 例如:
  - git push origin m, 不论怎样都是把本地m分支推送到远程m分支, 和你的工作分支没有一毛钱关系


## 参考文档

- [7.6 Git 工具 - 重写历史](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E9%87%8D%E5%86%99%E5%8E%86%E5%8F%B2)
- mac机设置可以参考茂弘的开源项目: [oh my mac](git@github.com:lornally/oh-my-mac.git)
- [关于pull和push的默认值](https://segmentfault.com/a/1190000002783245)
- [给pull和push设置不同分支](https://stackoverflow.com/questions/45638858/how-to-set-up-branches-with-different-pull-push-upstreams) [更多](https://stackoverflow.com/questions/2916845/different-default-remote-tracking-branch-for-git-pull-and-git-push)

