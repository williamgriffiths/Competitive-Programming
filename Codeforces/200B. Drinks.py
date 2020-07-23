n = int(input(""))
p = input("")
p = list(map(int, p.split()))
ans = 0

for num in p:
    ans += num

print(ans/len(p))


