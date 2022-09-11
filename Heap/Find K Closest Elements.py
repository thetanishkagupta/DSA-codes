# k - no of closest elements wanted.
# x - k elements closest to x in array

class Solution(object):
    def findClosestElements(self, arr, k, x):
        max_heap = []
        ans = []
        for i in range(len(arr)):
            diff = abs(arr[i] - x)
            heappush(max_heap,[diff, arr[i]])
        for i in range(k):
            diff, val = heappop(max_heap)
            ans.append(val)
        ans.sort()
        return ans

      
      
'''      
 5 6 7 8 9
 K = 3
 X = 7 
 Diff -> (7-5) (7-6) (7-7) (8-7) (9-7)
           2     1     0     1     2
 sort -> 0 1 1 2 2 
         7 6 8 5 9
 ans -> 7 6 8
'''
