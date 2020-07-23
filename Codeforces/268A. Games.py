n = int(input())
count = 0

home = []
away = []

for i in range(n):
    ha = input()
    h,a = (int(i) for i in ha.split())
    home.append(h)
    away.append(a)
    
for j in range(n):
    for k in range(n):
        if home[j] == away[k]:
            count += 1
        elif home[j] == away[k]:
            count += 1

print(count)
