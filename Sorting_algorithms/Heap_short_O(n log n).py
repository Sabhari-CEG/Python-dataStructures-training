
class Heap():
    def __init__(self):
        self.heap = [0]
        self.size = 0

    #during inserting we just add to last
    #we need to float the last element top based on their value
    def _float(self,k):
        while (k // 2) > 0:
            if self.heap[k//2] > self.heap[k]:
                self.heap[k//2],self.heap[k] = self.heap[k],self.heap[k//2]
            k = k//2

    def insert(self,data):
        self.heap.append(data)
        self.size += 1
        self._float(self.size)

    def _minindex(self,k):

        if ((k * 2) + 1) > self.size:
            return k * 2

        if self.heap[k*2] < self.heap[(k*2)+1]:
            return k*2
        else:
            return (k*2)+1

    def _sink(self,k):
        while k*2 < self.size:
            mi = self._minindex(k)
            if self.heap[mi] < self.heap[k]:
                self.heap[mi], self.heap[k] = self.heap[k],self.heap[mi]
            k = mi

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._sink(1)
        return item

    def HeapShort(self):
        sorted_list = []
        for i in range(self.size):
            sorted_list.append(self.pop())
        return sorted_list


if __name__ == '__main__':
    h = Heap()
    for i in (4,8,7,2,9,5,1,10,3,6):
        h.insert(i)

    print('heap is\t',h.heap)

    print(h.HeapShort())