alist =[54,226,93,17,77,31,44,55,28]
for i in range(1,len(alist)):
    for j in range(0,i)[::-1]:
         if alist[i]<alist[j]:
             alist[i],alist[j] =alist[j],alist[i]
             i-=1
    print(alist)
    print("-----")
