knw = input("")
k,n,w = (int(i) for i in knw.split())

cost = 0
total = 0

for i in range(1,w+1):
    total += i
    
cost += total*k

if cost > n:
    print(cost-n)
else:
    print(0)
