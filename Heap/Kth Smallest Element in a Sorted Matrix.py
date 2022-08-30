class Solution(object):
    def kthSmallest(self, matrix, k):
        max_heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                heappush(max_heap, -matrix[i][j])
                while len(max_heap) > k:
                    print(heappop(max_heap))
        return -heappop(max_heap)            
                    
