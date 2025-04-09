first_number = int(input())
second_number = int(input())
third_number = int(input())

first_number_first_digit = first_number // 10
first_number_second_digit = first_number % 10

second_number_first_digit = second_number // 10
second_number_second_digit = second_number % 10

third_number_first_digit = third_number // 10
third_number_second_digit = third_number % 10

if first_number_first_digit == second_number_first_digit == third_number_first_digit:
    print(first_number_first_digit)
elif first_number_second_digit == second_number_second_digit == third_number_second_digit:
    print(first_number_second_digit) 