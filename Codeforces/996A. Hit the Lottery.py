n = int(input())
bills = [100,20,10,5,1]
ans = 0

for i in bills:
    ans += n//i
    n = n % i

print(ans)
