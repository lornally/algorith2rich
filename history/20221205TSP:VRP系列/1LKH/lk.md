- https://en.wikipedia.org/wiki/Lin%E2%80%93Kernighan_heuristic
- https://en.wikipedia.org/wiki/2-opt
- https://en.wikipedia.org/wiki/3-opt

### 核心问题

- 交换点的时候, 如果点发生反转, 是否要反转中间的线路?

### 2opt

- 交换交叉线路, 形成不交叉的线路
- route:整体路径, v1交换的第一个线段的起点, v2交换的第二个线段的起点
- 新路径= route0到routev1的路径 
  - 加 route[v1+1]点到routev2点的路径取反向 
  - 加 route[v2+1]到结尾的路径

path=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,0]
new_path = path[:]
new_path[i:j] = path[j-1:i-1:-1]

### 3opt

```python
# 定义了反向交换
def reverse_segment_if_better(tour, i, j, k):
    """If reversing tour[i:j] would make the tour shorter, then do it."""
    # Given tour [...A-B...C-D...E-F...]
    A, B, C, D, E, F = tour[i-1], tour[i], tour[j-1], tour[j], tour[k-1], tour[k % len(tour)]
    d0 = distance(A, B) + distance(C, D) + distance(E, F)
    d1 = distance(A, C) + distance(B, D) + distance(E, F) # c..b反转
    d2 = distance(A, B) + distance(C, E) + distance(D, F) # d..e反转
    d3 = distance(A, D) + distance(E, B) + distance(C, F) # d..e前置, b..c后置
    d4 = distance(F, B) + distance(C, D) + distance(E, A) # fa交换

    if d0 > d1:
        tour[i:j] = reversed(tour[i:j])
        return -d0 + d1
    elif d0 > d2:
        tour[j:k] = reversed(tour[j:k])
        return -d0 + d2
    elif d0 > d4:
        tour[i:k] = reversed(tour[i:k])
        return -d0 + d4
    elif d0 > d3:
        tmp = tour[j:k] + tour[i:j]
        tour[i:k] = tmp
        return -d0 + d3
    return 0
# 3opt
def three_opt(tour):
    """Iterative improvement based on 3 exchange."""
    while True:
        delta = 0
        for (a, b, c) in all_segments(len(tour)):
            delta += reverse_segment_if_better(tour, a, b, c)
        if delta >= 0:
            break
    return tour

def all_segments(n: int):
    """Generate all segments combinations"""
    return ((i, j, k)
        for i in range(n)
        for j in range(i + 2, n)
        for k in range(j + 2, n + (i > 0)))
```

### LKH

- ab 替换为 ac, bd为d回到大本营, 只要保证ac<ab, 并且 ac+bd(回营)<ab+cd
- 处理回营的bd, 思路同上, d链接某个位置更短, 再次替换
  - 处理d是因为d是一个回营路线, 不一定很好
  - b其实之前被处理过了, ab就是打断了b的一边, 然后作为营地被d连接
- 处理新的回营连接, 在本轮尝试中, b一直作为营地存在

### 微信Y给的思路

- 3opt, 6个点ab..cd..ef, 
- 此时af, bc, de中间很多点, 可以认为他们是一个整体
- ab, cd, ef是相邻点, 因此可以打断关系形成交换
- 具体的4种交换, 对应winry的图片中的下方的4种3opt的全交换
- ac..be..df 反向bc, 反向de
- ad..ec..bf 反向bc, 正向de前置
- ae..db..cf 正向bc后置, 反向de
- ad..eb..cf 直接移动, 前后互换

### LK和爬山

- LK可以认为是找到周围最佳解的办法, 他是一种局部搜索, 沿着一个方向进行探索
- 因此, LK可以认为是爬山
- 模拟退火是针对爬山的改进, 他会接受一定的洼地方向

### 链式LK

- LK优化之后, 跳出最优解
- 比如做一次随机4opt任意4对点, 做交换链接
- 然后, 再次LK

### 遗传

- 很容易形成多个局部最优解
- 然后, 通过2opt, 杂交2条路线, 得到联合最优解
- EXA非常有效, edge-assembly crossover 边交叉
- 这个可能可以和最远插入结合起来


### LK原始优化思路
Lin-Kernighan启发式算法（LKH）的具体实现方法和优化策略如下：

###### Lin-Kernighan移动算子
Lin-Kernighan移动算子是LKH算法的核心。它是一种用于交换路径中的边以生成新的路径的方法。具体来说，算法从当前路径中选择两个点，然后尝试交换它们之间的边，以获得更短的路径。这个过程会不断地重复，直到无法找到更好的路径为止。

实现Lin-Kernighan移动算子的关键在于如何选择交换的边。具体来说，算法会选择一个起点和一个终点，然后依次选择从起点出发的每条边，对于每条边，算法会选择一条可以连接到终点的边，然后计算路径长度的变化，选择路径长度变化最小的边作为交换的边。

###### 动态规划预处理
- LKH算法使用动态规划来预处理路径，以加速算法的运行。具体来说，算法会计算出两点之间的最短路径，并将结果存储在一个距离矩阵中。在LKH算法运行时，可以通过查询距离矩阵的方式来快速计算路径长度的变化。
- 在1000点以下的问题中, 设置一个中间点

###### 分支限界法加速搜索
LKH算法使用分支限界法来加速搜索。具体来说，算法会将当前路径划分为若干段子路径，并使用分支限界法来搜索每个子路径的最优解。这样可以避免搜索整个路径空间，从而减少搜索时间。
具体实现上，可以使用递归的方式来实现分支限界法。每次递归，算法会选择一个子路径进行搜索，并计算出该子路径的下界。如果下界比当前最优解还要差，则可以剪枝，否则继续搜索。
例如, 
1. 将n个城市的路径分解为n段小路径, 每个小路径包含相邻的2个城市.
2. 每次优化一个小路径, 此时要保证连通性和合法性
3. 计算代价和界限函数, 界限是指代价和上界的差值, 上界通过最优解计算
例如，
1. 对于一个包含5个城市的TSP问题，假设初始解为城市1-城市2-城市3-城市4-城市5-城市1，
2. 可以将其分解成5个小路径：城市1-城市2、城市2-城市3、城市3-城市4、城市4-城市5、城市5-城市1。
3. 然后，选择其中一个小路径进行优化，例如城市3-城市4，使用2-opt算法进行优化，得到新的路径城市3-城市1-城市2-城市4。
4. 计算该路径的代价和限界函数，如果该路径的限界函数小于已知的最优解，可以剪枝，即跳过该路径，继续搜索其他路径。这样可以不断改进候选解，并最终找到全局最优解。


###### 随机化选择交换的边
为了增加搜索空间，LKH算法使用随机化来选择交换的边。具体来说，算法会在所有可选的边中随机选择一个交换的边，而不是选择路径长度变化最小的边。

###### 禁忌搜索
为了避免陷入局部最优解，LKH算法使用禁忌搜索来限制算法的搜索空间。具体来说，算法会记录已经搜索过的路径，并将其添加到禁忌表中。在搜索过程中，算法会避免选择已经在禁忌表中的路径，从而增加搜索空间。

以上就是LKH算法的具体实现方法和优化策略。具体实现时，可以根据算法的原理和流程编写代码，并根据实际情况进行调整和优化。

### 参考论文
* 原始论文LK1971.pdf
* 5opt改进论文LKH_report.pdf
* https://en.wikipedia.org/wiki/3-opt
* 4opt: https://isd.ktu.lt/it2011/material/Proceedings/1_AI_5.pdf
* lkh的wiki, 有Python实现: https://en.wikipedia.org/wiki/Lin%E2%80%93Kernighan_heuristic
* lkh论文: https://citeseerx.ist.psu.edu/doc/10.1.1.180.1798
* http://tsp-basics.blogspot.com/2017/03/3-opt-move.html
* https://blog.csdn.net/qq_30977037/article/details/117356753