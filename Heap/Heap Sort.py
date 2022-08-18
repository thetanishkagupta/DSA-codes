class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        largest = i
        left_child = (2*i)+1 
        right_child = (2*i)+2
        while left_child < n and arr[left_child] > arr[largest]:
            largest = left_child
        while right_child < n and arr[right_child] > arr[largest]:
            largest = right_child  
        if largest != i:
            arr[largest] , arr[i] = arr[i] , arr[largest]
            self.heapify(arr,n,largest)
        
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n//2-1, -1, -1):
            self.heapify(arr,n,i)
          
        
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        for i in range(n-1,-1,-1):
            arr[0] , arr[i] = arr[i] , arr[0]
            self.heapify(arr,i,0)
