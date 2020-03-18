list1=[4,1,1,9,1]
'''
不能选择相邻的数字
'''
list2 =[]
def DFS(list1):
    global list2
    if list1==[]:
        print(list2)
    for i in range(len(list1)):
        list2.append(list1[i])
        list3 =list1[::]
        DFS(list3[i+2:])
        list2.pop()
DFS(list1)


# 递归求解
arr =[1,2,4,1,7,8,3]
def rec_opt(arr,i):
    if i ==0:
        return arr[0]
    elif i==1:
        return max(arr[0],arr[1])
    else:
        A =rec_opt(arr,i-2)+arr[i]
        B =rec_opt(arr,i-1)
        return max(A,B)
a = rec_opt(arr,6)
print(a)

import numpy as np
def dp_opt(arr,i):
    opt = np.zeros(len(arr))
    opt[0] =arr[0]
    opt[1] =max(arr[0],arr[1])
    for i in range(2,len(arr)):
        A = opt[i-2]+arr[i]
        B = opt[i-1]
        opt[i] = max(A,B)
    return  opt[len(arr)-1]
print(dp_opt(arr,6))


arr=[3,34,4,12,5,2]
def rec_subset(arr,i,s):
    if s==0:
        return True
    elif i ==0:
        return arr[0]==s
    elif arr[i]>s:
        return rec_subset(arr,i-1,s)
    else:
        A =rec_subset(arr,i-1,s-arr[i])
        B =rec_subset(arr,i-1,s)
        return  A or B
print(rec_subset(arr,len(arr)-1,9))


