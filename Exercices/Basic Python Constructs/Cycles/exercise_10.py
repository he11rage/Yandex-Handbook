x = 0
y = 0

while (name := input()) != "СТОП":
    steps = int(input())

    if name == "СЕВЕР":
        x += steps
    elif name == "ЮГ":
        x -= steps
    elif name == "ВОСТОК":
        y += steps
    else:
        y -= steps

print(x)
print(y)
