#Stack data structure to keep track of biggest element
class StackWithBig:
    def __init__(self):
        self.mainStack = [] #main stack to store elements
        self.trackStack = [] #stack to keep track of the biggest element
    #push method tp add element to stack
    def push(self, x):
        self.mainStack.append(x) #append element to main stack
        if len(self.mainStack) == 1:
            self.trackStack.append(x) #if the stack is empty, append the element
            return
        #if current element is greater than the top ele of the track stack,
        #append the current ele to track stack otherwise append the ele at
        #the top of the stack again
        if x > self.trackStack[-1]:
            self.trackStack.append(x)
        else:
            self.trackStack.append(self.trackStack[-1])
    #function to get the biggest ele from the track stack
    def getBig(self):
        return self.trackStack[-1]

    def pop(self):
        self.mainStack.pop() # remove the top element from main stack
        self.trackStack.pop() # remove the top element from track stack

# Function to find the next bigger element for each element in the stack
def next_bigger_values(stack):
    result = {} #dictionary to store the result
    max_stack = StackWithBig() # initialize stack with the biggest ele

    #loop thru the stack form left to tright
    for elem in reversed(stack):
        #push ele to the stack
        max_stack.push(elem)
        # get the next bigger ele
        next_bigger = max_stack.getBig()

        # If the next bigger element is not the current element,
        # add it to the result dictionary, otherwise set the value to None
        if next_bigger != elem:
            result[elem] = next_bigger
        else:
            result[elem] = None

    return result


stack = [5, 3, 2, 10, 6, 8, 1, 4, 12, 7, 4]
result = next_bigger_values(stack)
for elem in stack:
    print(f"{elem} -> {result[elem]}")

#output:
'''
5 -> 12
3 -> 12
2 -> 12
10 -> 12
6 -> 12
8 -> 12
1 -> 12
4 -> 12
12 -> None
7 -> None
4 -> 12
'''
