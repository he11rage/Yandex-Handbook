first_str = input()
second_str = input()
third_str = input()

str_contains = []

for str in [first_str, second_str, third_str]:
    if "зайка" in str:
        str_contains.append(str)
        
result = min(str_contains)        
print(f"{result} {len(result)}")
        