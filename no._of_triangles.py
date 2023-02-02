# Python3 function to count all possible triangles with arr[]
# elements


def findnumberofTriangles(arr):

	# Sort array and initialize count as 0
	n = len(arr)
	arr.sort()
	count = 0

	# Fix the first element. We need to run till n-3 as
	# the other two elements are selected from arr[i + 1...n-1]
	for i in range(0, n-2):

		# Initialize index of the rightmost third element
		k = i + 2

		# Fix the second element
		for j in range(i + 1, n):

			# Find the rightmost element which is smaller
			# than the sum of two fixed elements
			# The important thing to note here is, we use
			# the previous value of k. If value of arr[i] +
			# arr[j-1] was greater than arr[k], then arr[i] +
			# arr[j] must be greater than k, because the array
			# is sorted.
			while (k < n and arr[i] + arr[j] > arr[k]):
				k += 1

			# Total number of possible triangles that can be
			# formed with the two fixed elements is k - j - 1.
			# The two fixed elements are arr[i] and arr[j]. All
			# elements between arr[j + 1] to arr[k-1] can form a
			# triangle with arr[i] and arr[j]. One is subtracted
			# from k because k is incremented one extra in above
			# while loop. k will always be greater than j. If j
			# becomes equal to k, then above loop will increment k,
			# because arr[k] + arr[i] is always greater than arr[k]
			if(k > j):
				count += k - j - 1

	return count


# Driver code
if __name__ == "__main__":
	arr = list(map(int, input().split(' ')))

	# Function call
	print("Total number of Triangles:", findnumberofTriangles(arr))

# This code is contributed by Devesh Agrawal
