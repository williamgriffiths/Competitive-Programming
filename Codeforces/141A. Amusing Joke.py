guest = input()
host = input()
guestChars = [i for i in guest]
hostChars = [i for i in host]

s = input()
sChars = [i for i in s]
ans = "YES"

for i in guestChars:
    if i in sChars:
        sChars.remove(i)
    else:
        ans = "NO"

for i in hostChars:
    if i in sChars:
        sChars.remove(i)
    else:
        ans = "NO"

if len(sChars) != 0:
    ans = "NO"

print(ans)
