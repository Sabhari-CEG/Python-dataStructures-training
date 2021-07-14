#node for singly linked list
class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class QueueBasedOnSinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Enqueue(self,data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def Dequeue(self):
        current = self.head
        if current:
            data = current.data
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return data
        return None

    def Traverse(self):
        current = self.head
        while current:
            print(current.data,end=' ')
            current = current.next

if __name__ == '__main__':
    queue = QueueBasedOnSinglyLinkedList()
    queue.Enqueue(1)
    print('after appending the first element')
    queue.Traverse()
    popped = queue.Dequeue()
    print("\nthe popped element is\t",popped)
    queue.Traverse()
    popped = queue.Dequeue()
    print("\nthe popped element is\t", popped)
    queue.Traverse()
    queue.Enqueue(1)
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Enqueue(4)
    queue.Enqueue(5)
    queue.Traverse()

