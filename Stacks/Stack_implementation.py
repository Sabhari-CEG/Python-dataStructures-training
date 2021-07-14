#create a node for stack
class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

#at next we create the stack class
class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    #we add the push function
    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    #we define the pop function
    def pop(self):
        if self.top:
            data = self.top.data
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            self.size -= 1
            return data
        return None

    def peek(self):
        if self.top:
            return self.top.data
        return None

if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(1)
    print("Peeking  the first element\n",my_stack.peek())
    print("poping the 1st element\n",my_stack.pop())
    print("peeking empty stack\n",my_stack.peek())
    print("poping empty stack\n",my_stack.pop())
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(5)
    print("peeking stack\n", my_stack.peek())
    print("poping stack\n", my_stack.pop())
    print("poping stack\n", my_stack.pop())
    print("poping stack\n", my_stack.pop())



