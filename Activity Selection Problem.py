def activitySelection(n, start, end):
    # Combine start and end time of activities in single list
    a = []
    for i in range(0, n):
        l = []
        l.append(start[i])
        l.append(end[i])
        a.append(l)
    # Sort the activities according to their end time
    a.sort(key=lambda x: x[1])
    i = 0
    output = []
    output.append(i)
    for j in range(1, len(a)):
        if a[j][0] >= a[i][1]:
            output.append(j)
            i = j
    return output
n = int(input())
s = list(map(int,input().split()))
e = list(map(int,input().split()))
res = activitySelection(n,s,e)
print(res)

'''
Input:-
6
1 3 0 5 8 5
2 4 6 7 9 9
Output:-
[0, 1, 3, 4]
'''



'''
Time Complexity:
    Case 1 : O(N), in case, the given array is sorted according to their finish times, where N is total steps.
    Case 2 : O(NlogN), in case, the given array is not sorted according to their finish times, where N is total steps.
    
'''
