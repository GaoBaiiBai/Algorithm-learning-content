# def quick_sort(alist):
#     n = len(alist)
#     mid_value = alist[0]
#     low =0
#     high = n-1
#     while  low<high:
#         while low <high and alist[high]>=mid_value :
#                  high-=1
#         alist[low] = alist[high]
#         low+=1
#         while low <high and alist[low]<mid_value :
#                 low +=1
#         alist[high] = alist[low]
#         high-=1
#     alist[low] = mid_value
#     print(alist)
# alist = [54,26,93,17,77,31,44,55,20]
# quick_sort(alist)


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
alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)