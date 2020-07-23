colors = input()
colors = list(map(int, colors.split()))

print(4 - len(set(colors)))
