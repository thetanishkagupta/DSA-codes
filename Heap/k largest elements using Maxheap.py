
import heapq
def kLargest(arr, n, k):
    maxheap = []
    for i in range(n):
        heapq.heappush(maxheap,-arr[i])
    ans = []
    for j in range(k):
        ans.append(-heapq.heappop(maxheap))
    return ans
    
A = [12, 5, 787, 1, 23]
N = 5
K = 2 
result = kLargest(A, N, K)
print(result)

# Output: [787, 23]

