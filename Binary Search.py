# mid = floor[(l+r)/2]
# CASE I: data == arr[mid]
# CASE II: data < arr[mid]
# CASE III: data > arr[mid]

n = int(input("length of array: "))
arr = list(map(int, input("elements of array : ").split()))
data = int(input("enter element to be searched: "))
found = 0
left = 0
right = n-1
while left <= right:
    mid = (left + right)//2
    if data == arr[mid]:
        print("Element found at index: ",mid)
        found = 1
        break
    elif data < arr[mid]:
        right = mid - 1 
    elif data > arr[mid]:
        left = mid + 1
if found == 0:        
    print("data is not present")        
