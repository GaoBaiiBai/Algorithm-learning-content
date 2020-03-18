class Stack(object):
    def __init__(self):
        self.list1 =[]
    def push(self,item):
        self.list1.append(item)

    def pop(self):
        return  self.list1.pop()
    def peek(self):
        if self.list1:
           return self.list1[-1]
    def is_empty(self):
        if len(self.list1) ==0:
            return False
        else:
            return True
    def size(self):
        return len(self.list1)
if __name__ == '__main__':
    s = Stack()

    print(s.is_empty())