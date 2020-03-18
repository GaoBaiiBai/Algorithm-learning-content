'''
# 最大公倍数和最大公约数
a =1125
b = 855
while a!=b:
    if a >b:
        a = a-b
    elif b>a:
        a,b=b,a
        a =a-b
print(a)


a =453
b = 36

if a>b:
    x=a
else:
    x=b
while True:
    if x%a==0 and x%b==0:
        print(x)
        break
    else:
        x+=1
# print(gcd(a,b))#最大公约数
'''
# 选择排序
alist =[54,226,93,17,77,31,44,55,28]
index_num =0
# j = 0
# while j <len(alist)-1:
for j in range(len(alist)-1):
    min_num = alist[j]
    index_num = j
    for i in range(j,len(alist)):
        if min_num >alist[i]:
            min_num = alist[i]
            index_num = i
    alist[j],alist[index_num]= alist[index_num],alist[j]
    j+=1
print(alist)
