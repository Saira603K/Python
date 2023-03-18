# Python3 program to print equal sum two subsets of
# an array if it can be partitioned into subsets.

# Function to print the equal sum sets of the array.
def printSets(set1, set2):
	# Print set 1.
	for i in range(len(set1)):
		print("{} ".format(set1[i]), end="")
	print("")

	# Print set 2.
	for i in range(len(set2)):
		print("{} ".format(set2[i]), end="")
	print("")

# Utility function to find the sets of the
# array which have equal sum.
def findSets(arr, n, set1, set2, sum1, sum2, pos):
	# If entire array is traversed, compare both
	# the sums.
	if (pos == n):
		# If sums are equal print both sets and
		# return true to show sets are found.
		if (sum1 == sum2):
			printSets(set1, set2)
			return True

		# If sums are not equal then return
		# sets are not found.
		else:
			return False

	# Add current element to set 1.
	set1.append(arr[pos])

	# Recursive call after adding current
	# element to set 1.
	res = findSets(arr, n, set1, set2, sum1 + arr[pos], sum2, pos + 1)

	# If this inclusion results in an equal sum
	# sets partition then return true to show
	# desired sets are found.
	if (res):
		return res

	# If not then backtrack by removing current
	# element from set1 and include it in set 2.
	set1.pop()
	set2.append(arr[pos])

	# Recursive call after including current
	# element to set 2 and removing the element
	# from set 2 if it returns False
	res = findSets(arr, n, set1, set2, sum1, sum2 + arr[pos], pos + 1)
	if not res:
		set2.pop()
	return res

# Return true if array arr can be partitioned
# into two equal sum sets or not.
def isPartitionPoss(arr, n):
	# Calculate sum of elements in array.
	sum = 0
	for i in range(n):
		sum += arr[i]

	# If sum is odd then array cannot be
	# partitioned.
	if (sum % 2 != 0):
		return False

	# Declare arrays to store both the sets.
	set1 = []
	set2 = []

	# Find both the sets.
	return findSets(arr, n,set1, set2, 0, 0, 0)

# Driver code
arr = [1, 3, 2, 1, 2, 1]
n = len(arr)
if not isPartitionPoss(arr, n):
	print("-1")

  
  #Output
 #1 3 1 
 #2 2 1
