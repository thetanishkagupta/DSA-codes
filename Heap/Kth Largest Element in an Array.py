from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = []
        
        # till Kth largest element push the elements in the heap 
        for i in range(k):            
            heappush(min_heap , nums[i])
         
        for i in range(k , len(nums)):
            if nums[i] > min_heap[0]:   # check if current element of num is greater than top(root) element of min_heap 
                heappop(min_heap)    # delete the root node of min_heap
                heappush(min_heap, nums[i])     # after deleting push the current element of nums
                
        return min_heap[0]         # return the top element of min_heap
        
