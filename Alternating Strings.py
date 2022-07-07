T = int(input())
while(T):
    n = int(input())
    S = input()
    ones, zero = 0, 0
    for char in S:
        if char == '0':
            zero += 1
        else:
            ones += 1 
    temp = min(zero,ones)
    if zero == ones:
        print(2*temp)
    else:
        print(2*temp + 1)
    T = T - 1
