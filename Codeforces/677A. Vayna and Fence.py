nh = input("")
n,h = (int(i) for i in nh.split())
ans = 0

heights = input("")
heights = list(map(int, heights.split()))

for height in heights:
    if height > h:
        ans += 2
    else:
        ans += 1

print(ans)
