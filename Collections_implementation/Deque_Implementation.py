#Deque is a double ended queue that can be append and removed from both ends.
import itertools
from collections import deque

if __name__ == '__main__':
    dq = deque('abc')
    print("Initial deque\n",dq)
    #append at end
    dq.append('d')
    print("after appending at end\n",dq)
    dq.appendleft('w')
    print("after appending to starting\n",dq)
    #extending at both ends
    dq.extend('efg')
    print("after extending at end\n",dq)
    dq.extendleft('xyz')
    print("after extending at beginning\n",dq)
    #pop at both ends
    popped = dq.pop()
    print("popped elem is ",popped,"\n",dq)
    popped = dq.popleft()
    print("popped elem is ", popped, "\n", dq)
    #we can rotate the queue
    dq.rotate(3)
    print("After rotating right by 3 elements\n",dq)
    dq.rotate(-4)
    print("After rotating left by 4 elements\n", dq)

    #slicing
    print("After slicing the deque")
    print(list(itertools.islice(dq,3,9)))

    #setting max length

    dq1 = deque([],maxlen=3)

    for i in range(10):
        dq1.append(i)
        print(dq1)

