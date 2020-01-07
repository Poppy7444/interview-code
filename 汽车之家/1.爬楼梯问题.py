# 上楼梯每次只能一步或者两步，有多少走法
# 动态规划最优解问题
# 上第n个台阶的方法 = 上第n-1个台阶的方法 + 上第n-2个台阶的方法

def go_up_stairs(floors: int):
    init_size = floors + 1 # 初始化数组容量
    if(floors < 2):
        init_size = 3
    ways = [0 for i in range(init_size)]
    ways[1] = 1
    ways[2] = 2
    for i in range(3,floors+1):
        ways[i] = go_up_stairs(i-1) + go_up_stairs(i-2)
    return ways[floors]