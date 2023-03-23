def find_consecutive_pairs(stack):
    if len(stack) < 2:
        print("Stack has less than 2 elements")
        return

    pairs = []
    prev_value = stack.pop()
    while stack:
        curr_value = stack.pop()
        #if statement, which uses abs(prev_value - curr_value) == 1
        # instead of prev_value - curr_value == 1.
        # This will detect consecutive pairs of numbers regardless of their order.
        if abs(prev_value - curr_value) == 1:
            pairs.append((prev_value, curr_value))
        prev_value = curr_value

    #The string is constructed using a list comprehension that iterates over the pairs
    # list and constructs a string representation of each pair in the format (x,y).
    # The resulting strings are then joined with commas using the join method.
    if pairs:
        pairs_str = ", ".join([f"({pair[0]},{pair[1]})" for pair in pairs])
        print(f"Result: Yes Consecutive pairs\n{pairs_str}")
    else:
        print("Result: No consecutive pairs found")


stack = [4, 5, -2, -3, 11, 10, 5, 6, 20]
find_consecutive_pairs(stack)

'''Output:
Result: Yes Consecutive pairs
(6,5), (10,11), (-3,-2), (5,4)
'''
