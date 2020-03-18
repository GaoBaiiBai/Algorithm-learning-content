'''
单链表
'''
class Node(object):
    """节点"""
    def __init__(self,elem):
        self.elem = elem
        self.next = None

# node = Node(100)
class SingleLinkList(object):
    def __init__(self,node=None):
        self._head =node

    def is_Empty(self):
        '''判断链表是否为空'''
        return self._head == None

    def length(self):
        '''链表长度'''
        cur = self._head
        count = 0
        while cur != None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        # number = self._head
        # print(number.next)
        # while number.next !=None:
        #     print(number.elem)
        #     number = number.next
        """遍历链表"""
        cur = self._head
        while cur != None:
            print (cur.elem)
            cur = cur.next
        print ("")


    def add(self,item):
        '''链表头部添加元素'''
        node = Node(item)
        if self.is_Empty():
            self._head = node
        else:
            node.next = self._head
            self._head=node
    def append(self,item):
        # '''链表尾部添加'''
        # node = Node(item)
        # if self.is_Empty():
        #     self._head= node
        #
        #     print(node.elem)
        # else:
        #     cur = self._head
        #     while cur.next !=None:
        #         cur =cur.next
        #     cur.next = node
        """尾部添加元素"""
        node = Node(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_Empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next =node 


    def insert(self,pos,item):
        def insert(self, pos, item):
            """指定位置添加元素"""
            # 若指定位置pos为第一个元素之前，则执行头部插入
            if pos <= 0:
                self.add(item)
            # 若指定位置超过链表尾部，则执行尾部插入
            elif pos > (self.length() - 1):
                self.append(item)
            # 找到指定位置
            else:
                node = Node(item)
                count = 0
                # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
                pre = self._head
                while count < (pos - 1):
                    count += 1
                    pre = pre.next
                # 先将新节点node的next指向插入位置的节点
                node.next = pre.next
                # 将插入位置的前一个节点的next指向新节点
                pre.next = node


    def remove(self,item):
        '''删除节点'''
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
    def search(self,item):
        '''判断链表是否存在'''
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
if __name__ == '__main__':
    ll = SingleLinkList()
    # ll.is_Empty()
    # ll.length()
    ll.add(8)
    ll.append(1)
    ll.add(9)
    ll.travel()