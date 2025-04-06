import math

a = float(input())
b = float(input())
c = float(input())
    
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
    exit()
elif a == 0:
    if b == 0:
        print("No solution")
    else:
        x = -c / b
        print(x)
    exit()
    
disc = b ** 2 - 4 * a * c  
if disc < 0:
    print("No solution")
elif disc == 0:
    sq = -b / (2 * a)
    print(sq)
else:
    first_sq = (-b + math.sqrt(disc)) / (2 * a)
    sec_sq = (-b - math.sqrt(disc)) / (2 * a)
    print(sec_sq, first_sq)