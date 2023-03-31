"""Given a circular queue with max size = M to save each element, after several times
enqueue (insert) & dequeue(delete) operations, front & rear have their own values,
write a function or method getNumElem(size, front, rear) to find how many
elements are in the circular queue"""

class CircularQueue:
    # Constructor
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 8

    # Adding elements to the queue
    def enqueue(self, data):
        if self.size() == self.maxSize - 1:
            return "Queue Full!"
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize
        return True

    # Removing elements from the queue
    def dequeue(self):
        if self.size() == 0:
            return "Queue Empty!"
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

    # Calculating the size of the queue
    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        return (self.maxSize - (self.head - self.tail))

def getNumElem(size, front, rear):
    return (rear - front + size) % size

q = CircularQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)

num_elems = getNumElem(q.maxSize, q.head, q.tail)
print(num_elems)

q.dequeue()
q.dequeue()
q.dequeue()

num_elems = getNumElem(q.maxSize, q.head, q.tail)
print(num_elems)

q.enqueue(9)
q.enqueue(10)

num_elems = getNumElem(q.maxSize, q.head, q.tail)
print(num_elems)

"""
Output
7
4
6
"""
