class Node(object):
    def __init__(self,item):
        self.elem =item
        self.lchid= None
        self.rchid = None
class Tree(object):
    def __init__(self):
        self.root = None
    def add(self,item):
        node =Node(item)
        if self.root  is None:
            self.root = node
            return
        queue=[self.root]
        while queue:
            cur_node =queue.pop(0)
            if cur_node.lchid is None:
                cur_node.lchid =node
                return
            else:
                queue.append(cur_node.lchid)
            if cur_node.rchid is None:
                cur_node.rchid = node
                return
            else:
                queue.append(cur_node.rchid)
    def breadth_travel(self):
        """
        广度遍历
        :return:
        """
        queue = [self.root]
        if self.root is None:
            return
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchid is not None:
                queue.append(cur_node.lchid)
            if cur_node.rchid is not None:
                queue.append(cur_node.rchid)
    def preorder(self,node):
        if node is None:
            return
        print(node.elem)
        self.preorder(node.lchid)
        self.preorder(node.rchid)
    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.lchid)
        print(node.elem)
        self.inorder(node.rchid)
    def postorder(self,node):
        if node is None:
            return
        self.postorder(node.lchid)
        print(node.elem)
        self.postorder(node.rchid)


if __name__ == '__main__':
    tree =Tree()
    tree.add(0)
    tree.add(9)
    tree.add(8)
    tree.add(7)
    tree.add(6)
    tree.add(5)
    tree.add(6)
    tree.add(3)
    tree.breadth_travel()
    tree.postorder(tree.root)
    tree.inorder(tree.root)
    tree.preorder(tree.root)





