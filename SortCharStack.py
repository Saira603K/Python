#Sort char type elements in stack
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def sort(self):
        temp_stack = Stack()
        while not self.is_empty():
            temp = self.pop()
            while not temp_stack.is_empty() and temp_stack.peek() > temp:
                self.push(temp_stack.pop())
            temp_stack.push(temp)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())


# Create a stack and push some characters onto it
stack = Stack()
stack.push('c')
stack.push('a')
stack.push('e')
stack.push('b')
stack.push('d')

# Print the original order of the stack
print("Original Stack: ", end="")
while not stack.is_empty():
    print(stack.pop(), end=" ")
print()

# Push the same characters back onto the stack in sorted order
stack.push('c')
stack.push('a')
stack.push('e')
stack.push('b')
stack.push('d')
stack.sort()

# Print the sorted order of the stack
print("Sorted Stack: ", end="")
while not stack.is_empty():
    print(stack.pop(), end=" ")
print()

stack2 = Stack()
stack2.push('n')
stack2.push('t')
stack2.push('s')
stack2.push('o')
stack2.push('r')

print("Original Stack: ", end="")
while not stack2.is_empty():
    print(stack2.pop(), end=" ")
print()

# Push the same characters back onto the stack in sorted order
stack2.push('n')
stack2.push('t')
stack2.push('s')
stack2.push('o')
stack2.push('r')
stack2.sort()
# Print the sorted order of the stack
print("Sorted Stack: ", end="")
while not stack2.is_empty():
    print(stack2.pop(), end=" ")
print()

'''Output:
Original Stack: d b e a c 
Sorted Stack: a b c d e 
Original Stack: r o s t n 
Sorted Stack: n o r s t 
'''
