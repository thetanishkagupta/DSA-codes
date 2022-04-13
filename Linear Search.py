n = int(input("length of array: "))
arr = list(map(int, input("elements of array : ").split()))
key = int(input("enter element to be searched: "))
found = 0
for i in range(0,n):
    if arr[i] == key:
        print("Element found at index: ", i)
        found = 1
        break
if(found == 0):
    print("Element not found")  
 
    
