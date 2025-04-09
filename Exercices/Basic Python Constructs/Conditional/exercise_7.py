number = int(input())

first_digit = number // 1000
second_digit = number % 1000 // 100
third_digit = number % 1000 % 100 // 10
fourth_digit = number % 1000 % 100 % 10

if first_digit == fourth_digit and second_digit == third_digit:
    print("YES")
else:
    print("NO")