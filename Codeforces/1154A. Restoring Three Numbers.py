xs = input()
x1,x2,x3,x4 = (int(i) for i in xs.split())
lst = sorted([x1,x2,x3,x4])

c = max(lst) - lst[2]
b = lst[1] - c
a = lst[0] - c
print(" ".join(str(i) for i in sorted([a,b,c])))
