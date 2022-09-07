# Sort a K Sorted Array | Sort Nearly Sorted Array

from heapq import *
class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        min_heap = []
        ans = [0]*n
        for i in range(0,n):
            heappush(min_heap,a[i])
            if i >= k:          # when i is greater than size of k then pop and store the minimum element in ans 
                ans[i-k] = heappop(min_heap)    # this will form the sorted array 
        while min_heap:         # when elements are present in min heap while array is traversed fully 
            ans[n-len(min_heap)-1] = heappop(min_heap)   # then pop those elements in ans , it will give the sorted array.
        return ans      
                
