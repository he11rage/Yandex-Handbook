first_speed = int(input())
second_speed = int(input())
third_speed = int(input())    

if first_speed < second_speed < third_speed:
    print("1. Толя")
    print("2. Вася")
    print("3. Петя")
elif second_speed < first_speed < third_speed:
    print("1. Толя")
    print("2. Петя")
    print("3. Вася") 
elif first_speed < third_speed < second_speed:
    print("1. Вася")
    print("2. Толя")
    print("3. Петя") 
elif third_speed < first_speed < second_speed:
    print("1. Вася")
    print("2. Петя")
    print("3. Толя") 
elif second_speed < third_speed < first_speed:
    print("1. Петя")
    print("2. Толя")
    print("3. Вася") 
elif third_speed < second_speed < first_speed:
    print("1. Петя")
    print("2. Вася")
    print("3. Толя") 