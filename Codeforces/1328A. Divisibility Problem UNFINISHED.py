t = int(input())
lst = []

for i in range(t):
    ab = input()
    a,b = (int(i) for i in ab.split())
    count = 0

    while a % b != 0:
        a += 1
        count += 1

    print(count)
