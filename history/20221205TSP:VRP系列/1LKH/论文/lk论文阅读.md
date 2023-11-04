### 总纲

1. Generate a pseudorandom feasible solution, that is, a set T that satisfies C.
2. Attempt to find an improved feasible solution T' by some transformation of T.
3. If an improved solution is found, i.e., f(T') <f(T), then replace T by T' and repeat from Step 2.
4. If no improved solution can be found, T is a locally optimum solution. Repeat from Step 1 until computation time runs out, or the answers are satisfactory.

1. 生成伪随机可行解，即满足C的集合T。
2. 尝试通过对 T 进行某种变换来找到改进的可行解 T'。
3. 如果找到改进的解，即 f(T') <f(T)，则将 T 替换为 T'，并从步骤 2 开始重复。
4. 如果找不到改进的解，则T 是局部最优解。 从步骤 1 开始重复，直到计算时间用完，或者答案令人满意。