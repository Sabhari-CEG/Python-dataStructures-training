#node for singly linked list
from random import randint
import time
class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None

class QueueBasedOnSinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def Enqueue(self,data):
        node = Node(data)
        if self.tail:
            node.prev = self.tail
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
                self.head.prev = None
            self.size -= 1
            return data
        return None

    def Traverse(self):
        current = self.head
        while current:
            print("song name:\t",current.data.title)
            print("Song length:\t",current.data.length)
            time.sleep(current.data.length)
            current = current.next

class Track():
    def __init__(self,title = None):
        self.title = title
        self.length = randint(5,10)

class MusicPlayerQueue(QueueBasedOnSinglyLinkedList):

    def __init__(self):
        super(MusicPlayerQueue, self).__init__()

    def add_track(self,track):
        self.Enqueue(track)

    def play(self):
        self.Traverse()


if __name__ == '__main__':
    track1 = Track('song 1')
    track2 = Track('song 2')
    track3 = Track('song 3')
    queue = MusicPlayerQueue()
    queue.add_track(track1)
    queue.add_track(track2)
    queue.add_track(track3)
    queue.play()


