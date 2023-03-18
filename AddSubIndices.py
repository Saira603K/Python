#Assuming that all int type values are saved in an array, find
#a function to get maximum value from a[u] – a[v] + a[w] –a[x], where indices must be
#u>v>w>x. will be the result based on given array

def max_difference(a):
    n = len(a)
    max_val = float('-inf')
    for u in range(n):
        for v in range(u):
            for w in range(v):
                for x in range(w):
                    max_val = max(max_val, a[u]-a[v]+a[w]-a[x])
    return max_val


# define the input array
a = [3, 9, 10, 1, 30, 40]

# call the max_difference function to find the maximum difference
max_diff = max_difference(a)

# print the result
print(max_diff)


# output: 46

