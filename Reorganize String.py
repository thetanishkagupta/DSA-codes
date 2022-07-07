from collections import Counter
from heapq import heapify, heappush, heappop

class Solution(object):
    def reorganizeString(self, s):
        c = Counter(s)
        output , temp = [], None
        
        maxheap = [(-count, char) for char, count in c.items()]  # Create a max heap of the counts
        heapify(maxheap)
        
        for i in range(len(s)):
            # If there's no character in the heap and we're still in the loop;
            # this string cannot be converted.
            if not maxheap:
                return ''
         
            temp2 = heappop(maxheap)   # Remove the most frequent character from the heap.
            
            # If the max freq is 0; there are no characters left but 
            # since we're still in the loop, this means that this string
            # cannot be converted.
            if temp2[0] == 0:
                return ''
            output.append(temp2[1])    # Append the most frequent character to the output.
            
            # Next time the count will be 1 less but since we're storing the 
            # negatives of counts (to simulate a max heap), add 1 to the count.
            temp2 = (temp2[0] + 1, temp2[1])
            if temp:
                heappush(maxheap,temp)   # If there's an element left from the last time; push it to the heap
            temp = temp2 if temp2[0] < 0 else None    # Next time, temp2 will be pushed to the heap
            
        return "".join(output)    
