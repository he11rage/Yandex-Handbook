number = int(input())

first_digit = number // 100
second_digit = number % 100 // 10
third_digit = number % 100 % 10

min_digit = min(first_digit, second_digit, third_digit)
max_digit = max(first_digit, second_digit, third_digit)


if min_digit == 0 and min_digit <= first_digit <= max_digit:
    print(f"{first_digit}{min_digit} {max_digit}{first_digit}")
elif min_digit == 0 and min_digit <= second_digit <= max_digit:
    print(f"{min_digit}{second_digit} {max_digit}{second_digit}")  
elif min_digit == 0 and min_digit <= third_digit <= max_digit:
    print(f"{min_digit}{third_digit} {max_digit}{third_digit}")
elif min_digit <= first_digit <= max_digit:
    print(f"{min_digit}{first_digit} {max_digit}{first_digit}")
elif min_digit <= second_digit <= max_digit:
    print(f"{min_digit}{second_digit} {max_digit}{second_digit}")
elif min_digit <= third_digit <= max_digit:
    print(f"{min_digit}{third_digit} {max_digit}{third_digit}")
      