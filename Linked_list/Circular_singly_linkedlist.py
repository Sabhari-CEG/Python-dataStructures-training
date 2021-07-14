#Create a node class
class Node():
    #node has data container and next container
    def __init__(self,data):
        self.data = data
        self.next = None

    #to represent the data present in node
    def __str__(self):
        return str(self.data)

#now create the singly linked list class
class CircularSinglyLinkedList():
    #initial settings for list
    #head is starting node, tail is ending node and initial size is 0
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #now we develope the append option
    def append(self,data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1
        self.tail.next = self.head

     # to travese the list
    def traverse(self):
        current = self.head
        i = 0
        while current:
            if i == 2 * self.size:
                break
            val = current.data
            current = current.next
            i+=1
            yield val

#delete based on data
    def delete(self,data):
        current = self.head
        prev = self.head
        while current == prev or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                    current.next = None
                elif current == self.tail:
                    prev.next = None
                    self.tail = prev
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                self.size -= 1
                return current
            prev = current
            current = current.next




if __name__ == '__main__':
    #n = Node('sabhari')
    #print(n)
    csl = CircularSinglyLinkedList()

    csl.append('first')
    print("after apending the first content")
    for word in csl.traverse():
        print(word)
    print("the size of the list is\t",csl.size)
    csl.append('second')
    csl.append('third')
    csl.append('fourth')
    print('after several appends')
    for word in csl.traverse():
        print(word)
    print("the size of the list is\t", csl.size)
    deleted = csl.delete('first')
    print("deleting first item\t", deleted)
    for word in csl.traverse():
        print(word)
    print("the size of the list is\t", csl.size)
    print("The head is\t", csl.head)
    deleted = csl.delete('fourth')
    print("deleting last item\t", deleted)
    for word in csl.traverse():
        print(word)
    print("the size of the list is\t", csl.size)
    print("The tail is\t", csl.tail)
    csl.append('fourth')
    csl.append('fifth')
    csl.append('sixth')
    print("after appending several items\n")
    for word in csl.traverse():
        print(word)
    print("the size of the list is\t", csl.size)
    deleted = csl.delete('fourth')
    print('after deleting the fourth at middle')
    for word in csl.traverse():
        print(word)
    print("the size of the list is\t", csl.size)

