'''
问题：假设一段楼梯共15个台阶，小明一步最多能上3个台阶，那么小明上这段楼梯一共有多少种方法？
'''
def step(n):
    if n ==1:
        return 1
    if n ==2:
        return 2
    if n ==3:
        return 3
    return step(n-1)+step(n-2)+step(n-3)
def climbStairs1(n):
    a = 1
    b = 2
    c = 4
    for i in range(n-3):
        c, b, a = a+b+c, c, b
    return c
if __name__ == '__main__':
    print(step(15))
    print(step(15))