# Create a function to simulate stack push & pop operations by using only ONE queue

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from queue import Queue

class Stack:
    def __init__(self):
        self.q = Queue()

    def push(self, val):
        # Enqueue the value to the back of the queue
        self.q.put(val)

        # Rotate the queue so that the last enqueued value is at the front
        for _ in range(self.q.qsize() - 1):
            self.q.put(self.q.get())

    def pop(self):
        # Dequeue the value at the front of the queue (which is the last enqueued value)
        return self.q.get()

    def is_empty(self):
        return self.q.empty()

stack = Stack()

# Push values onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Pop values from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2

# Check if the stack is empty
print(stack.is_empty())  # Output: False

# Push more values onto the stack
stack.push(4)
stack.push(5)

# Pop all remaining values from the stack
print(stack.pop())  # Output: 5
print(stack.pop())  # Output: 4
print(stack.pop())  # Output: 1

# Check if the stack is empty again
print(stack.is_empty())  # Output: True

"""
Output
3
2
False
5
4
1
True
"""
