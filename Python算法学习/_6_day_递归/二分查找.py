# list1=[17, 20, 26, 31, 44, 54, 55, 77, 93]
import numpy as  np
list1=[17,20]
def zheban(list1,n):
    start = 0
    end = len(list1)
    index = (start+end)//2
    while start!=end:
        if list1[index]>n:
            end =index
            index=(start+end)//2
        if list1[index]<n:
            start=index
            index =(start+end)//2
        if list1[index]==n:
            return True
        if start==end-1:
            return False
def search(list2,target,start,end):
    left= start
    righ =end
    if left==end-1:
        return False
    mid = int((left+righ)/2)
    if list2[mid]==target:
        return True
    elif list2[mid]<target:
        return search(list2[mid:righ],target,mid,righ)
    elif list2[mid]>target:
        return search(list2[left:mid],target,left,righ)
 # print(zheban(list1,57))
print(search(list1,21,0,len(list1)))
print(zheban(list1,20))
data_list = np.linspace(0,5,50)
print(np.arange(0,6,0.5))
print(len(data_list))
print(data_list)