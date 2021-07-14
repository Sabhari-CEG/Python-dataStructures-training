#implementing queue concept using the inbuilt list function
class ListBasedQueue():
    def __init__(self):
        self.item = []
        self.size = 0

    #we will just insert data at beginning
    def Enqueue(self,data):
        self.item.insert(0,data)
        self.size += 1

    #we will pop at end for dequeue
    def Dequeue(self):
        data = self.item.pop()
        self.size -= 1
        return data

    #we will traverse the list
    def Traverse(self):
        for element in self.item:
            print(element,end=' ')

if __name__ == '__main__':
    queue = ListBasedQueue()
    queue.Traverse()
    queue.Enqueue(1)
    print("after 1st entry")
    queue.Traverse()
    print("\nafter several entry")
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Enqueue(4)
    queue.Enqueue(5)
    queue.Traverse()
    popped = queue.Dequeue()
    print("\nthe popped element is\t",popped)
    queue.Traverse()
    popped = queue.Dequeue()
    print("\nthe popped element is\t", popped)
    queue.Traverse()