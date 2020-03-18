# list1 = [1,2,7,8,9]
# list1 = [5,8,9,6,5,2,6,2]
# list1 = [14,9,12,15]
list1 =[3,5,6,9,12,15]
'''
[3,5,6,9,12,15]
[8,6,9,12,15]
[14,9,12,15]
[14,21,15]
[21,29]
'''
index = 0
while list1 !=[]:
    if len(list1)==2:
        print('左右结合', "left:", list1[0], "right:", list1[1], "节点", list1[0] + list1[1])
        break
    if index==0:
        print('左边', "left:", list1[0], "right:", list1[1], "节点", list1[0] + list1[1])
        list1[1] = list1[0] + list1[1]
        list1.pop(0)
        index += 1
    if list1[2]>=list1[0]>=list1[1] or list1[1]>=list1[0]>=list1[1]:
        print('左边',"left:",list1[0],"right:",list1[1],"节点",list1[0]+list1[1])
        list1[1] = list1[0] + list1[1]
        list1.pop(0)
    elif list1[0]>=list1[1] and list1[0] >=list1[2]:
        print('右边', "left:", list1[1], "right:", list1[2], "节点", list1[1] + list1[2])
        list1[2] = list1[1] + list1[2]
        list1.pop(1)
    elif list1[0]<list1[1] and list1[0]<list1[1]:
        print('左边', "left:", list1[0], "right:", list1[1], "节点", list1[0] + list1[1])
        list1[1] = list1[0] + list1[1]
        list1.pop(0)

# 使用优先级队列遍历哈夫曼树
import queue
q = queue.PriorityQueue()
list1 =[3,5,6,9,12,15]
for i in list1:
    q.put(i,str(i))
while q.empty() ==False:
    if q.qsize()==1:
        s = q.get()
        print("根节点",s)
        break
    a = q.get()
    b = q.get()
    print("节点",a,"节点",b,"子节点:",a+b)
    q.put(a+b,str(a+b))