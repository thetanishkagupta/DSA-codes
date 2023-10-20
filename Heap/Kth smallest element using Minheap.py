
import heapq
def kthSmallest(arr, n, k):
    minheap = []
    for i in range(n):
        heapq.heappush(minheap,arr[i])
    ans = []
    for j in range(k):
        ans.append(heapq.heappop(minheap))
    return ans[-1]   
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
n = len(arr)
k = 4
print(kthSmallest(arr,n, k))

# Output: 5

