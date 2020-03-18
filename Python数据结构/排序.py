def maopao(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]= list1[j+1],list1[j]
    return list1
def xuanze(list1):
    for j in range(len(list1)):
        index =j
        min_num = list1[j]
        for i in range(j,len(list1)):
            if list1[i]<min_num:
                index = i
        list1[j],list1[index]= list1[index],list1[j]
    return list1
def charu(list1):
    for i in range(0,len(list1)):
        j = i
        while j!=0:
            if list1[j]<list1[j-1]:
                list1[j],list1[j-1]=list1[j-1],list1[j]
                j-=1
            else:
                break
    return list1
def quick_sort(alist,start,end):
    if start>=end:
        return
    mid_value = alist[start]
    low =start
    high = end
    while  low<high:
        while low <high and alist[high]>=mid_value :
                 high-=1
        alist[low] = alist[high]

        while low <high and alist[low]<mid_value :
                low +=1
        alist[high] = alist[low]
    alist[low] = mid_value
    quick_sort(alist,0,low-1)
    quick_sort(alist,low+1,end)
    print(alist)
if __name__ == '__main__':
    list1 =[54,26,93,17,77,31,44,55,20]
    # print(maopao(list1))
    # print(xuanze(list1))
    # print(charu(list1))
    print(quick_sort(list1,0,len(list1)-1))