w1w2 = input("")
w1,w2 = (int(i) for i in w1w2.split())

years = 0
while w1 <= w2:
    w1 *= 3
    w2 *= 2
    years += 1

print(years)
