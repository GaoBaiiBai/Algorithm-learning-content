class Queue(object):
    def __init__(self):
        self.__list = []
    def enqueue(self,item):
        self.__list.append(item)
    def dequeue(self):
        return self.__list.pop(0)
    def is_empty(self):
        if self.__list ==[]:
            return False
    def size(self):
        return  len(self.__list)
if __name__ == '__main__':
    q = Queue()
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print (q.size())
    print (q.dequeue())
    print (q.dequeue())
    print (q.dequeue())