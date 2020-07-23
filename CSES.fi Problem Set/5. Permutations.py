n = int(input(""))
lst = [i for i in range(1,n+1)]
beautiful = []

if 1 < n < 4:
    print("NO SOLUTION")

for i in range(2, n+1, 2):
    beautiful.append(str(i))

for i in range(1, n+1, 2):
    beautiful.append(str(i))
    
print(" ".join(beautiful))
