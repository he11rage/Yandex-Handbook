number = int(input())
res = 1
for i in range(number + 1):
    if (i == 0):
        res = 1 * res
    else:
        res = i * res
    
print(res)