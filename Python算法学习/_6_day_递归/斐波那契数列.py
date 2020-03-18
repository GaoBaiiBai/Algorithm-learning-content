'''
1、1、2、3、5、8、13、21、34
'''
import time
k =0
def Fn(n):
    global k
    if n ==1 or n ==2:
        return 1
    k+=1
    return Fn(n-1)+Fn(n-2)
def fib(n):
    assert  n>0,"n必须大于0"
    if n ==1 or n ==2:
        return 1
    num1 =1
    num2=1
    for i in range(2,n):
        num = num1+num2
        num2 =num1
        num1 =num
    return num
if __name__ == '__main__':
    start_time=time.time()
    print(Fn(34))
    print(k)
    end_time = time.time()
    print(end_time-start_time)
    start_time=time.time()
    print(fib(3))
    end_time = time.time()
    print(end_time-start_time)