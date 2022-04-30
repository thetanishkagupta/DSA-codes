class Solution:
    def bubbleSort(self,arr, n):
        for i  in range(n-1):
            for j in range(n-1-i):  # to avoid extra checking at the last which happens in every pass
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                j += 1
            i += 1
        return arr
