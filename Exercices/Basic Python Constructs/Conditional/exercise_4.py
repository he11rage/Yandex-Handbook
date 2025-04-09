petya_apple = 7
vasya_apple = 6

n = int(input())
m = int(input())

result_count_petya_apples = petya_apple - 3 + 2 + n
result_count_vasya_apples = vasya_apple + 5 - 2 + m

if result_count_petya_apples > result_count_vasya_apples:
    print("Петя")
else:
    print("Вася")    
