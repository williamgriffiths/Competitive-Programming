n = int(input(""))
p = input("")
p = list(map(int, p.split()))
output = []

for i in range(1,n+1):
    output.insert(i,p.index(i)+1)

print(" ".join([str(i) for i in output]))
