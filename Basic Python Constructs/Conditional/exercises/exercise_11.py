number = int(input())

first_digit = number // 100
second_digit = number % 100 // 10
third_digit = number % 100 % 10

min_digit = min(first_digit, second_digit, third_digit)
max_digit = max(first_digit, second_digit, third_digit)

if min_digit < first_digit < max_digit and min_digit + max_digit == first_digit * 2:
    print("YES")
elif min_digit < second_digit < max_digit and min_digit + max_digit == second_digit * 2:
    print("YES")
elif min_digit < third_digit < max_digit and min_digit + max_digit == third_digit * 2:
    print("YES")       
else:
    print("NO")