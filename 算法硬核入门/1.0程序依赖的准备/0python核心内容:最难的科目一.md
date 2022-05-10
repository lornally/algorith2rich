> 最难的就是万里长征的第一步, 因此, 这个文档的难度是冠绝整个教程系列的, 所以, 有任何问题大家速度反馈, 不要害羞, 出问题是正常的. 不出问题是奇迹
### 为什么学python
- 算法领域, python建模已经成为王道
- 原因: 
 - 语法简洁易懂
  - 相对于java, 很简洁, 
  - 相对于c,  R(lisp变体), 很易懂
 - 相对于ruby, 他的库非常丰富
 - 虽然python本体运行速度很慢, 但是可以直接调用c库, 因此速度问题比较容易解决
- 简单说: 综合能力最好, 是一个6边型战士

### 入门准备
1. 准备一台mac, 任意mac都可以, macOS10.15之后的版本都可以, 当前(2022.3.16)最新版本是12.2.1
2. 后续主要都是命令行操作, 因此需要安装oh-my-zsh
```sh
# 打开命令行, mac默认安装了terminal, 建议小白直接使用系统这个
# 安装oh-my-zsh
sh -c "$(curl -fsSL https://gitee.com/pocmon/ohmyzsh/raw/master/tools/install.sh)"
```
3. 后续需要安装管理各种软件包, 因此需要包管理器brew.
```sh
# 安装包管理器brew
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```
4. 可选项目: 安装编辑器 
  - 如果你习惯其他编辑器, 例如: textmate, sublime, vi, emacs... 
  - 那么都是可以的 
  - 不需安装这个
```sh
# 如果没有文本编辑器, 建议安装visual-studio-code, 
brew install visual-studio-code
```
5. 安装python包管理工具anaconda
```sh
brew install anaconda
```

### 检验一下入门准备: 启动python notebook
> 目标: 进入工作目录, 一般情况是在自己的document目录新建一个notebook目录, 步骤如下

1. 进入自己的根目录
```sh
~ 
pwd # 检查一下当前目录

```
2. 进入自己的document目录
```sh
docu # 此时按一下tab键, 会发现自动补全了目录名, 然后按enter, 就进入document目录了
pwd # 再检查一下目录
```
3. 新建一个notebook目录
```sh
makedir nb # nb是我的目录名, 大家可以任意给一个自己喜欢的目录名
nb #进入刚刚的目录名
```
4. 启动notebook
```sh
ipython notebook
# 此时会看到类似黑河帝国的经典命令行滚动画面
```
> 此时的正确结果: 系统会自动打开一个浏览器, 不论是safari还是chrome都是OK的, 如果safari有兼容问题, 建议使用brew安装chrome:
```sh
brew install google-chrome
```
> 恭喜你, 大功告成, 咱们可以happy的编程了(点击右上角的new->python3就出现了新的页面)

### 附录: 可选项目, 为notebook启动设置快捷方式
```sh
code ~/.zshrc
# 这里code是启动virtual-studio-code, 如果使用其他编辑器请使用对应的编辑命令
```
- 在编辑界面, 文档的尾部录入以下内容
```sh
# notebook
alias pn="ipython notebook"
# 这里/Users/machangkun/Documents/__ipython_notebook是我的工作目录, 请换成你的对应目录
alias pnn="jupyter notebook --notebook-dir=/Users/machangkun/Documents/__ipython_notebook"
```

> 最难的就是万里长征的第一步, 因此, 这个文档的难度是冠绝整个教程系列的, 所以, 有任何问题大家速度反馈, 不要害羞, 出问题是正常的. 不出问题是奇迹