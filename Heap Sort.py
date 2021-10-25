def MAX_HEAPIFY(a,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and a[largest] < a[l]:
          largest = l
    if r < n and a[largest] < a[r]:
          largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        MAX_HEAPIFY(a,n,largest)
def BUILD_MAX_HEAP(a,n):   
    for i in range(n//2-1,-1,-1):
        MAX_HEAPIFY(a,n,i)
def HEAP_SORT(a,n):
    BUILD_MAX_HEAP(a,n)
    for i in range(n-1,-1,-1):
        a[i],a[0] = a[0], a[i]
        MAX_HEAPIFY(a,i,0)
n = int(input("Enter number of elements: "))
a = list(map(int,input("Enter array elements: ").strip().split()))
HEAP_SORT(a,n)
print("Sorted Array: ",*a) 
