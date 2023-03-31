#For each element in a given queue is char type and priority of each element
#is ASCII code value, write functions to complete push and pop operations

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        priority = ord(item)
        heapq.heappush(self.heap, (-priority, item))

    def pop(self):
        if len(self.heap) > 0:
            priority, item = heapq.heappop(self.heap)
            return item
        else:
            raise IndexError("pop from an empty priority queue")

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if len(self.heap) > 0:
            priority, item = self.heap[0]
            return item
        else:
            return None

    def pop_highest_priority(self):
        if len(self.heap) > 0:
            highest_priority = self.peek()
            while self.peek() == highest_priority:
                heapq.heappop(self.heap)
            return highest_priority
        else:
            raise IndexError("pop from an empty priority queue")


pq = PriorityQueue()

# Insert items with priorities
pq.push('C')
pq.push('O')
pq.push('D')
pq.push('A')

# Remove the item with the highest priority
pq.pop_highest_priority()  # 'o' is popped out

# Print the remaining items in the priority queue
#while not pq.is_empty():
    #print(pq.pop())  # Output: D C A

pq.push('B')
# Remove the item with the highest priority
pq.pop_highest_priority()  # 'd' is popped out

# Print the remaining items in the priority queue
while not pq.is_empty():
    print(pq.pop())  # Output: C B A
    
    
    
