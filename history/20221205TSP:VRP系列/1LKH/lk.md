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

- 3opt, 6个点ab..cd..ef
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