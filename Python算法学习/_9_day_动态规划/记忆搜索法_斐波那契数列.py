total ={}
# 搜索+记忆
def fib_desk(k):
    if k ==1:
        return 1
    if k ==2:
        return 1
    if k in total:
        result = total[k]
    else:
        result=fib_desk(k - 1) + fib_desk(k - 2)
        total[k] = result
    return  result
if __name__ == '__main__':
    print(fib_desk(36))
    print(total)