n = int(input(""))
count = 0

for i in range(n):
    pq = input("")
    pq = list(map(int, pq.split()))
    p,q = pq[0], pq[1]

    if q-p >= 2:
        count += 1

print(count)
