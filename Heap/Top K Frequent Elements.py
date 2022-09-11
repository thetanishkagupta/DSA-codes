'''
k = 2
1 1 1 3 2 2 4
create hashmap (dict)
arr[i]     Freq
  1    ->   3
  3    ->   1
  2    ->   2
  4    ->   1
  
Traverse the hashmap and put it into the min_heap on Freq basis
[(3,1)]        K = 1
[(3,1) (1,3)]  K = 2
[(3,1) (2,2) (1,3)]   K = 3  which is greater than K value so pop 
[(3,1) (2,2)]  k = 2
[(3,1) (2,2) (1,4)] K = 3 so pop
[(3,1) (2,2)]   k = 2

[ 2   ,  2
  3   ,  1 ]
 freq ,  arr[i]
 
 so now print arr[i] as ans
'''

class Solution(object):
    def topKFrequent(self, nums, k):
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        min_heap = []
        for i in dict.keys():
            heappush(min_heap, (dict[i], i))
            if len(min_heap) > k:
                heappop(min_heap)
        ans =[]
        for f,i in list(min_heap):
            ans.append(i)
        return ans     
                
