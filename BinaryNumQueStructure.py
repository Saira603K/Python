"""Write a function or method with positive int type argument, such as genBin(7), and
outputs will be binary number sequence from 110 to 710, like 12, 102, 112,1002
,1012,1102, 1112 by using queue structure
"""

from collections import deque

def genBin(n):
    """
    Generate binary number sequence from 1*1 to n*1 using a queue.
    """
    # Initialize the queue with the binary number '1'.
    q = deque(['1'])

    # List to store the generated binary numbers.
    binary_nums = []

    # Loop until we generate n binary numbers.
    while len(binary_nums) < n:
        # Pop the first element from the queue and add it to the list of binary numbers.
        num = q.popleft()
        binary_nums.append(num)

        # Generate the next two binary numbers by appending '0' and '1' to the current number.
        q.append(num + '0')
        q.append(num + '1')

    # Return the list of generated binary numbers.
    return binary_nums

binary_nums = genBin(10)
binary_nums1 = genBin(5)
binary_nums2 = genBin(7)
print(binary_nums)
print(binary_nums1)
print(binary_nums2)

"""
Output
['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010']
['1', '10', '11', '100', '101']
['1', '10', '11', '100', '101', '110', '111']
"""
