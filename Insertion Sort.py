n = int(input("no element: "))
arr = list(map(int,input("Enter elements of array: ").split()))
for i in range(n):
    temp = arr[i] # starting from index 1 of the array 
    j = i - 1     # 1-1 i.e arr[0]
    while j >= 0 and arr[j] > temp:   # loop for comparison
        arr[j+1] = arr[j]
        j -= 1 
    arr[j+1] = temp
    i+=1    
print(arr)    
        
        
    
