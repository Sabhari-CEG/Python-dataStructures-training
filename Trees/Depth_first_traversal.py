class Node():
    def __init__(self,data = None):
        self.data = data
        self.left_child = None
        self.right_child = None

class BinarySearchTree():
    def __init__(self):
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current.data

    def find_max(self):
        current = self.root_node
        while current.right_child:
            current = current.right_child
        return current.data

    def insert(self,data):
        current = self.root_node
        parent = None
        node = Node(data)
        if current is None:
            self.root_node = node
        else:
            while True:
                parent = current
                if node.data <= current.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return

    def get_node_with_parent(self,data):
        parent = None
        current = self.root_node
        if current is None:
            return (None,None)
        while True:
            if current.data == data:
                return (parent,current)
            elif data <= current.data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent,current)

    def remove(self,data):
        parent,node = self.get_node_with_parent(data)

        if (parent is None) and (node is None):
            return False

        children_count = 0

        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1
        print("no of child\t",children_count)

        if children_count == 0:
            #print("entered")
            if parent:
                if parent.left_child == node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            else:
                self.root_node = None

        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            if parent:
                if parent.left_child == node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node

        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child

    def search(self,data):
        current = self.root_node
        while current:
            if current is None:
                return False
            if current.data == data:
                return True
            elif data <= current.data:
                current = current.left_child
            else:
                current = current.right_child

    def inorder_traverse(self,root_node):
        current = root_node
        if current is None:
            return
        self.inorder_traverse(current.left_child)
        print(current.data)
        self.inorder_traverse(current.right_child)

    def preorder_traverse(self,root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.preorder_traverse(current.left_child)
        self.preorder_traverse(current.right_child)

    def postorder_traverse(self,root_node):
        current = root_node
        if current is None:
            return
        self.preorder_traverse(current.left_child)
        self.preorder_traverse(current.right_child)
        print(current.data)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(9)
    tree.insert(1)
    tree.insert(4)
    tree.insert(7)
    tree.insert(10)
    print('Inorder')
    print(tree.inorder_traverse(tree.root_node))
    print('preorder')
    print(tree.preorder_traverse(tree.root_node))
    print('post order')
    print(tree.postorder_traverse(tree.root_node))



