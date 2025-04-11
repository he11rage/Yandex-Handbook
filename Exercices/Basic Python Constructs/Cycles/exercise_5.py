total = 0

while (price := float(input())) != 0:
    if price >= 500:
        total += price - price * 0.1
    else:
        total += price
else:
    print(total)