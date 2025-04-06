# Синтаксис

yesterday_temp = int(input())
today_temp = int(input())
if today_temp > yesterday_temp:
    print("Сегодня теплее, чем вчера.")
elif today_temp < yesterday_temp:
    print("Сегодня холоднее, чем вчера.")
else:
    print("Сегодня такая же температура, как вчера.")
    
# операции сравнения
print(4 > 5) # Больше
print(4 >= 5) # Больше или равно 
print(4 < 5) # Меньше 
print(4 <= 5) # Меньше или равно 
print(4 == 5) # Равно 
print(4 != 5) # Не равно

#Логические операции

print(4 and 5 > 0) # И
print(4 or 5 > 4) # ИЛИ
print(not 4 or 5 > 4) # НЕ

# ord - получить код символа

print(ord("d"), ord("w"))

# chr - получить символ по коду

print(chr(116), chr(119))

m = 12
n = 19
k = 25

# максимальное число
print(max(m, n, k))

line_1 = "m"
line_2 = "n"
line_3 = "k"

# минимальная лексикографически строка
print(min(line_1, line_2, line_3))

# количество цифр в числе 2 в степени 2022
print(len(str(2 ** 2022)))