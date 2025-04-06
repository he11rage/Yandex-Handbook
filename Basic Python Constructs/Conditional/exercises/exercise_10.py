number = int(input())

first_digit = number // 100
second_digit = number % 100 // 10
third_digit = number % 100 % 10

first_part = second_digit + third_digit
second_part = first_digit + second_digit

print(f"{max(first_part, second_part)}{min(first_part, second_part)}")
