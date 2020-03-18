a = [1,12,3,45,66,6.655,66,56,56516,516,516,5]
print(set(a))
dict1 ={}
for i in a:
    dict1[i] = dict1.get(i,0)+1
print(dict1)
for i in a:
    dict1[i] = dict1.get(i,0)
print(dict1)
# 贪心算法
# 孩子的需求
g =[5,10,2,9,15,9]
# 孩子的糖果数
s =[6,1,20,3,8]
# 冒泡排序

def maopao_sort(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1
g = maopao_sort(g)
s = maopao_sort(s)
print(g)
print(s)

back =0
s_back =0
num =0
while back<len(g):
    if g[back]<=s[s_back]:
        num +=1
        back+=1
        if s_back ==len(s)-1:
            break
    elif s_back ==len(s)-1:
        break
    s_back+=1
print(num)