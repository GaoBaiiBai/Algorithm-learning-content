list1 = [
    [13],
    [11, 8],
    [12, 7, 26],
    [6, 14, 15, 8],
    [12, 17, 13, 24, 11]
]
high = len(list1) - 1
def guihua(list1,cen_list1=[]):
    global high
    if high==0:
        print(cen_list1)
        return
    max_list=[]

    if high==len(list1) - 1:
        for i in  range(len(list1[high])-1):
            if list1[high][i]>list1[high][i+1]:
                max_list.append(list1[high][i])
            else:
                max_list.append(list1[high][i+1])
        high-=1
        cen_list=[]
        for i,q in zip(list1[high],max_list):
            cen_list.append(i+q)
        guihua(list1,cen_list)

    else:
        for i in  range(len(cen_list1)-1):
            if cen_list1[i]>cen_list1[i+1]:
                max_list.append(cen_list1[i])
            else:
                max_list.append(cen_list1[i+1])
        high-=1
        cen_list=[]
        for i,q in zip(list1[high],max_list):
            cen_list.append(i+q)
        guihua(list1,cen_list)

guihua(list1)