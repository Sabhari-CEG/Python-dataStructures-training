#a simple node to implement trees
class Node():
    def __init__(self,data = None):
        self.data = data
        self.left_child = None
        self.right_child = None

if __name__ == '__main__':
    n1 = Node('Root')
    n2 = Node('left child')
    n3 = Node('right child')
    n4 = Node('left grand child')

    n1.left_child = n2
    n1.right_child = n3
    n2.left_child = n4

    current = n1
    while current:
        print(current.data)
        current = current.left_child