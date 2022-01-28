from math import sqrt
num = int(input("Enter the number: "))
result = []      # We will store all factors in `result`
i = 1

# This will loop from 1 to int(sqrt(x))
while i <= int(sqrt(num)):
    if num % i == 0:         # Check if i divides x without leaving a remainder
        if i * i == num:     
            result.append(i)
        else:
            result.append(i)
            result.append(num // i)
    i += 1
print("Factors of the given number are: ",*result)
