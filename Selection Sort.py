n = int(input("no element: "))
arr = list(map(int,input("Enter elements of array: ").split()))
for i in range(n-1):   
    mini = i 
    for j in range(i+1,n):
        if arr[j] < arr[mini]:
            mini = j
    if mini != i:
        arr[i],arr[mini] = arr[mini] , arr[i]
print(arr)        
