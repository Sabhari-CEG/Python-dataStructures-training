#here we have both the prev and next pointer
class Node():
    #container for data,prev and next
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    #to get the string representation
    def __str__(self):
        return str(self.data)

#doubly linked list class
class DoublyLinkedList():
    #initial conditions
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    #first we make function to traverse list
    def traverse(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    #we also make function for reverse traversal
    def ReverseTraversal(self):
        current = self.tail
        while current:
            val = current.data
            current = current.prev
            yield val

    #append data to list
    def append(self,data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.count += 1

    #to delete an element
    def delete(self,data):
        current = self.head
        node_deleted = False

        if current is None:
            return

        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True

        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count -= 1

    #searching for item
    def search_for(self,data):

        for word in self.traverse():
            if word == data:
                return True
        return False


if __name__ == '__main__':
    dl = DoublyLinkedList()
    dl.append('first')
    print("after adding first element to list")
    for word in dl.traverse():
        print(word)
    print('The size of list is\t',dl.count)
    dl.append('second')
    dl.append('third')
    dl.append('fourth')
    dl.append('fifth')
    print("after adding several items the forward and reverse traversal are")
    print('=====forward=====')
    for word in dl.traverse():
        print(word)
    print("=====reverse=====")
    for word in dl.ReverseTraversal():
        print(word)
    print('The size of list is\t',dl.count)

    dl.delete('third')
    print("after deleting in middle")
    print('=====forward=====')
    for word in dl.traverse():
        print(word)
    print("=====reverse=====")
    for word in dl.ReverseTraversal():
        print(word)
    print('The size of list is\t', dl.count)

    dl.delete('first')
    print("after deleting at beginning")
    print('=====forward=====')
    for word in dl.traverse():
        print(word)
    print("=====reverse=====")
    for word in dl.ReverseTraversal():
        print(word)
    print('The size of list is\t', dl.count)

    dl.delete('fifth')
    print("after deleting last")
    print('=====forward=====')
    for word in dl.traverse():
        print(word)
    print("=====reverse=====")
    for word in dl.ReverseTraversal():
        print(word)
    print('The size of list is\t', dl.count)
    print("fourth in list?",dl.search_for('fourth'))
    print("first"
          " in list?", dl.search_for('first'))



