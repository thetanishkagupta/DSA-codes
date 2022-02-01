# one method

def partition( arr, lb, ub):
    pivot = arr[lb]
    start = lb + 1
    end = ub
    while True:
        while (start <= end and arr[start] <= pivot):
            start += 1
        while (start <= end and arr[end] >= pivot):
            end -= 1
        if (start < end):
            arr[start], arr[end] = arr[end], arr[start]
        else:
            break
    arr[lb], arr[end] = arr[end], arr[lb]
    return end


def quickSort(arr, lb, ub):
    if lb < ub:
        loc = partition(arr, lb, ub)
        quickSort(arr, lb, loc - 1)
        quickSort(arr, loc + 1, ub)


arr = list(map(int, input("enter the elements: ").split()))
quickSort(arr, 0, len(arr)-1)
print('Sorted Array in Ascending Order:')
print(arr)


# second method

class Solution:
    def quickSort(self,arr,low,high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

        
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while (i <= j and arr[i] <= pivot):
                i = i + 1
            while (i <= j and arr[j] >= pivot):
                j = j - 1
            if (j < i):
                break
            else:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j
    
