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

def priority(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0

def InfixToPostfix(statement):
    stack = Stack()
    stack.push('#')
    size = 0
    result = ""
    for element in statement:
        print(element)
        if element == '(':
            print("found '(' and pushing in")
            stack.push(element)
        elif element.isalnum():
            result += element + ' '
            print("simply a number and the result is \t", result)
        elif element in ('+','-','*','/','^'):
            prior = priority(element)
            if stack.peek() == '(':
                stack.push(element)
                size += 1
            elif priority(stack.peek()) < prior:
                stack.push(element)
                size += 1
            elif priority(stack.peek()) >= prior:
                result += stack.pop() + ' '
                stack.push(element)
        elif element == ')':
            while True:
                val = stack.pop()
                if val == '(':
                    break
                result += val + ' '
                size -= 1
    while size > 0:
        result += stack.pop() + ' '
        print("final pop out\t",result)
        size -= 1
    return result

if __name__ == '__main__':
    a = '(4+8)*(6-5)/((3-2)*(2+2))'
    print("result:\n",InfixToPostfix(a))

