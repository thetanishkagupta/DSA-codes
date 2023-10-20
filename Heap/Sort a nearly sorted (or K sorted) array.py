import heapq
arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
minheap = []
for i in range(min(k + 1, len(arr))):     # Push the first (k + 1) elements into the min-heap
    heapq.heappush(minheap, arr[i])       # Now, minheap contains the first 4 elements in a min-heap: [2, 3, 5, 6]

index = 0
for i in range(k + 1, len(arr)):          # Process the remaining elements of the array
    arr[index] = heapq.heappop(minheap)   # Pop the smallest element from the min-heap and put it in the original array at index 'index'
    heapq.heappush(minheap, arr[i])       # Push the current element from 'arr' into the min-heap
    index += 1                            # Now, arr contains the first 4 elements sorted in ascending order, and minheap contains [5, 8, 9, 10].

while minheap:                            # Add any remaining elements from the min-heap to the end of 'arr'
    arr[index] = heapq.heappop(minheap)
    index += 1                            # Now, the remaining elements in minheap (5, 8, 9, 10) are added to the end of 'arr'.
print(arr)                                # The final sorted 'arr' is [2, 3, 5, 6, 8, 9, 10]

# Output: [2,3,5,68,9,10]   

