nt = input("")
n,t = (int(i) for i in nt.split())

s = input("").upper()

for i in range(t):
    s = s.replace("BG","GB")

print(s)
