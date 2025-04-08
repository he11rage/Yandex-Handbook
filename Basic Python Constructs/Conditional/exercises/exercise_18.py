first_number = int(input())
second_number = int(input())
third_number = int(input())

a = 0
b = 0
hypo = max(first_number, second_number, third_number)

if hypo == first_number:
    a = second_number
    b = third_number
elif hypo == second_number:
    a = first_number
    b = third_number
else:
    a = first_number
    b = second_number

if a ** 2 + b ** 2 == hypo ** 2:
    print("100%")
elif a ** 2 + b ** 2 < hypo ** 2:
    print("велика")
else:
    print("крайне мала")    