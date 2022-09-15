'''
 Sort the array in increasing order based on the frequency of the values. 
 If multiple values have the same frequency, sort them in decreasing order.
 '''
class Solution(object):
    def frequencySort(self, nums):
        d={}
        max_heap=[]
        heapify(max_heap)
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for k,v in d.items():
            heappush(max_heap,(v,-k))
        res=[]
        for i in range(len(d)):
            pop=heappop(max_heap)
            val=pop[1]*-1
            for i in range(pop[0]):
                res.append(val)
        return res
