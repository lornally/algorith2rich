> 注意学习的过程中, 每个代码都要手打, 不要复制粘贴
### 界面熟悉

```python
# 打开notebook, 录入代码
3+5
# 此时ctrl+enter, 就可以执行代码看到结果

x=10
x+5
# ctrl+enter一下, 看看结果

y= x+11
y
# ctrl+enter一下, 看看结果

# * 生成一个数组
list(range(19))
# 这个要解释一下, range会制造一个可以数的集合, list会把这个集合转化为数组列表, 看不懂这行没关系, 忽略他就好了.

# 录入下面代码, 然后ctrl+enter
for n in range(10):
 print(f'数数:{n}')
# 这里是一个循环for 和in都是关键字, range之前学过, print是打印

# 修改一下这个循环
for n in range(10):
 print(f'数字:{n}的平方:{n*n}')


# * 定义一个函数试试
def ave(x,y): # 这里x,y是参数
 a=(x+y)/2.0 # 这里计算平均数, 这是python比较蠢的地方, 2.0代表结果可能有小数, 如果用2, 他就自动帮你取整.
 return a # 这里定义了返回值

# 此处执行刚刚定义的函数
ave(2,4) #这里是一次调用, 2,4是参数, 大家可以尝试换一下试试

# * 数组(list)
import numpy as np
a = np.zeros([3,2])
a
# ctrl-enter执行一下试试

a[2,1]=9
a[0,1]=8
a
# ctrl-enter执行一下试试
# 自己尝试更改更多值试试, 例如
a[30,50]=8 # 这里会报错, 想想为什么报错



v=a[2,1]
v
# ctrl-enter试试


# 数据可视化
import matplotlib.pyplot as plt

# 这一行是魔术指令, 可以简单理解为是个设置
%matplotlib inline

# 绘图
plt.imshow(a)

# 绘图, 这里要指出的第二个参数是不要平滑图像颜色, 也就是不同颜色硬画, 
plt.imshow(a, interpolation='nearest')

```

### 附录: 更进一步
> 推荐廖雪峰的教程(不需要看面向对象部分以及之后的部分): https://www.liaoxuefeng.com/wiki/1016959663602400/1016966022717728
- 推荐阅读内容:
 - python基础
 - 函数
 - 高级特性
 - 函数式编程
- 从模块开始就不建议阅读了
- 尤其不建议阅读面向对象的相关内容, 思路和做法都非常曲折复杂, 是上个世纪80年代的风格, 在飞速发展的计算机领域, 属于代码的古代写法
- 如果这样还是觉得内容太多了, 没关系, 咱们有极简版本