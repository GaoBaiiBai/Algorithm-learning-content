list1 = [
    [13],
    [11, 8],
    [12, 7, 26],
    [6, 14, 15, 8],
    [12, 17, 13, 24, 11]
]
max_value=0
info={}
def search_max(depth,y):
    if depth==4:
        return list1[depth][y]

    # 1、把下方的值交给下一个人得到最大值
    left_max = search_max(depth+1,y)
    # 2、把右下方的值交给下一个人得到最大值
    # 1、任务可以下分 2、最优子结构 3、决策
    right_max= search_max(depth+1,y+1)
    return list1[depth][y]+max(left_max,right_max)
print(search_max(0,0))