n = int(input(""))
x = 0

for i in range(n):
    X = input("")
    if "X" and "++" in X:
        x += 1
    if X and "--" in X:
        x -= 1

print(x)
