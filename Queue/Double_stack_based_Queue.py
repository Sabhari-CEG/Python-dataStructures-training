#use two stacks to implement queue
class DoubleStackBasedQueue():

    #use two list for stacks
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    #enqueue happens at the inbound stack
    def Enqueue(self,data):
        self.inbound_stack.append(data)

    #during dequeue the element is removed from outbound queue
    def Dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()

if __name__ == '__main__':
    queue = DoubleStackBasedQueue()
    queue.Enqueue(1)
    print("First item added\nInbound stack\t",queue.inbound_stack,'\nOutbound stack\t',queue.outbound_stack)
    queue.Enqueue(2)
    queue.Enqueue(3)
    queue.Enqueue(4)
    queue.Enqueue(5)
    print("Inbound stack\t", queue.inbound_stack, '\nOutbound stack\t', queue.outbound_stack)
    popped = queue.Dequeue()
    print('Popped element is\t',popped)
    print("Inbound stack\t", queue.inbound_stack, '\nOutbound stack\t', queue.outbound_stack)
    queue.Enqueue(6)
    queue.Enqueue(7)
    print("Inbound stack\t", queue.inbound_stack, '\nOutbound stack\t', queue.outbound_stack)
    for i in range(0,6):
        popped = queue.Dequeue()
        print('Popped element is\t', popped)
        print("Inbound stack\t", queue.inbound_stack, '\nOutbound stack\t', queue.outbound_stack)

