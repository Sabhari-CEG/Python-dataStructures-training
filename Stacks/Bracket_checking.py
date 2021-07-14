class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

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

def Bracket_checking(statement):
    stack = Stack()
    popped = None
    for element in statement:

        if element in ('(','{','['):
            stack.push(element)
        if element in (')','}',']'):

            popped = stack.pop()
            
            if popped == '{' and element == '}':
                continue
            elif popped == '(' and element == ')':
                continue
            elif popped == '[' and element == ']':
                continue
            else:
                print("mismatch")
                return False
    if stack.size > 0:
        print("size greater")
        return False
    else:
        return True

if __name__ == '__main__':
    sl = (
        "{(foo)(bar)}[hello](((this)is)a)test", "{(foo)(bar)}[hello](((this)is)atest",
        "{(foo)(bar)}[hello](((this)is)a)test))"
    )
    for s in sl:
        m = Bracket_checking(s)
        print("{}: {}".format(s, m))