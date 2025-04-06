fir_sp, sec_sp, thr_sp = int(input()), int(input()), int(input())

list = [("Петя", fir_sp), ("Вася", sec_sp), ("Толя", thr_sp)]

list.sort(key=lambda x: x[1], reverse=True)

first = list[0][0]

second = list[1][0]

third = list[2][0]

print(f'{"": ^8}{first: ^8}{"": ^8}')
print(f'{second: ^8}{"": ^8}{"": ^8}')
print(f'{"": ^8}{"": ^8}{third: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')