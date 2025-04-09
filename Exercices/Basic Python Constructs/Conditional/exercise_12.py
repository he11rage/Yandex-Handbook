first_number = int(input())
second_number = int(input())
third_number = int(input())

a = first_number + second_number
b = first_number + third_number
c = third_number + second_number

if a > third_number and b > second_number and c > first_number:
    print("YES")
else:
    print("NO")
