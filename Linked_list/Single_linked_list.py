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
class SinglyLinkedList():
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

    #to travese the list
    def traverse(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    #delete based on data
    def delete(self,data):
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    current.next = None
                elif current == self.tail:
                    prev.next = None
                    self.tail = prev
                else:
                    prev.next = current.next
                self.size -= 1
                return current
            prev = current
            current = current.next

    #to search whether the element is present in the list
    def Search_for(self,data):
        for word in self.traverse():
            if data == word:
                return True
        return False

    #to clear entire list
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    #insert based in index
    def insert(self,data,index):
        current = self.head
        prev = self.head
        index_count = 0
        while current:
            node = Node(data)
            if index_count == index:
                if current == self.head:
                    node.next = self.head
                    self.head = node
                else:
                    prev.next = node
                    node.next = current
                self.size += 1
                return
            prev = current
            current = current.next
            index_count += 1
        print("Index out of range")
        return -1

    #delete based on index
    def remove(self,index):
        current = self.head
        prev = self.head
        index_count = 0
        while current:
            if index_count == index:
                if current == self.head:
                    self.head = current.next
                    current.next = None
                elif current == self.tail:
                    prev.next = None
                    self.tail = prev
                else:
                    prev.next = current.next
                self.size -= 1
                return current
            prev = current
            current = current.next
            index_count += 1


if __name__ == '__main__':
    #n = Node('sabhari')
    #print(n)
    sl = SinglyLinkedList()

    sl.append('first')
    print("after apending the first content")
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t",sl.size)
    sl.append('second')
    sl.append('third')
    sl.append('fourth')
    print('after several appends')
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t", sl.size)
    deleted = sl.delete('first')
    print("deleting first item\t",deleted)
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t", sl.size)
    print("The head is\t",sl.head)
    deleted = sl.delete('fourth')
    print("deleting last item\t", deleted)
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t", sl.size)
    print("The tail is\t", sl.tail)
    sl.append('fourth')
    sl.append('fifth')
    sl.append('sixth')
    print("after appending several items\n")
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t", sl.size)
    deleted = sl.delete('fourth')
    print('after deleting the fourth at middle')
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t", sl.size)
    print("fourth in list?",sl.Search_for('fourth'))
    print("third in list?", sl.Search_for('third'))
    sl.insert('first',0)
    print('after inserting at beginning')
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t", sl.size)
    print("The head is\t",sl.head)
    sl.insert('fourth',3)
    print('after inserting at 3rd index')
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t", sl.size)
    sl.insert('tenth',9)
    print("for index not present in the list")
    removed = sl.remove(3)
    print('after removing 3rd index\t',removed)
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t", sl.size)
    print("finally clearing the list")
    sl.clear()
    for word in sl.traverse():
        print(word)
    print("the size of the list is\t", sl.size)






