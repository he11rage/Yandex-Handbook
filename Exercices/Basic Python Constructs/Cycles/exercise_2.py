count = 0
while (str := input()) != "Приехали!":
    if "зайка" in str:
        count += 1
else:
    print(count)