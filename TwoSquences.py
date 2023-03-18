def find_sequences(N):
    # create the list with 2*N elements
    lst = []
    for i in range(1, N+1):
        lst.append(i)
        lst.append(i)
    
    # initialize the result list
    sequences = []
    
    # iterate over the elements in the list
    for i in range(len(lst)):
        # calculate the required distance
        dist = lst[i]
        
        # iterate over the elements that come after i in the list
        for j in range(i+1, len(lst)):
            # check if the distance is equal to the value of the element
            if lst[j] == dist:
                # if so, add the sequence to the result list
                sequences.append(lst[i:j+1])
    
    return sequences

print(find_sequences(3))
[[1, 2], [2, 1, 3], [3, 2]]
print(find_sequences(4))

#Output
//[[1, 1], [2, 2], [3, 3]]
[[1, 1], [2, 2], [3, 3], [4, 4]]//
