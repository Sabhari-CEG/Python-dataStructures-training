
class Heap():
    def __init__(self):
        self.heap = [0]
        self.size = 0

    #during inserting we just add to last
    #we need to float the last element top based on their value
    def _float(self,k):
        while (k // 2) > 0:
            if self.heap[k//2] < self.heap[k]:
                self.heap[k//2],self.heap[k] = self.heap[k],self.heap[k//2]
            k = k//2

    def insert(self,data):
        self.heap.append(data)
        self.size += 1
        self._float(self.size)

    def _maxindex(self,k):

        if ((k * 2) + 1) > self.size:
            return k * 2

        if self.heap[k*2] > self.heap[(k*2)+1]:
            return k*2
        else:
            return (k*2)+1

    def _sink(self,k):
        while k*2 < self.size:
            mi = self._maxindex(k)
            if self.heap[mi] > self.heap[k]:
                self.heap[mi], self.heap[k] = self.heap[k],self.heap[mi]
            k = mi

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._sink(1)
        return item


if __name__ == '__main__':
    h = Heap()
    for i in (4,8,7,2,9,10,5,1,3,6):
        h.insert(i)

    print('heap is\t',h.heap)

    for i in range(10):
        print("popped\t",h.pop())
        print("heap is\t",h.heap)