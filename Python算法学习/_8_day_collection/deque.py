from collections import deque
userlist=deque(("1","2","3"))
user_name = userlist.popleft()
userlist1=["1","2","3"]
user_name1=userlist1.pop(0)
print(user_name1)
print(user_name)
from queue import Queue
yyy=Queue()
print(yyy.empty())
yyy.put(5)
print(yyy.empty())
yyy.get(2,0.5)
print(yyy.qsize())
# deque GIL是线程安全的，list不是线程安全的
# deque的拷贝是浅拷贝，虽然id不同,但是dequeue里是一个对象的时候，也会改变
user_deque= deque(["bobby1",["bobby2","bobby3"],"bobby3"])
user_deque_copy = user_deque.copy()
user_deque[1].append(1)
user_deque[0]="1"
print(user_deque)
print(user_deque_copy)
'''
# 深拷贝
import copy
deep=copy.deepcopy(user_deque)
# 动态的扩容
deque.extend()
'''
list1=[1,2,5,8,9]
list1.pop(0)
list1.insert(0,5)
print(list1)