nk = input("")
n,k = (int(i) for i in nk.split())

scores = input("")
scores = list(map(int, scores.split()))

count = 0

for i in range(n):
    if scores[i] >= scores[k-1] and scores[i] > 0:
        count += 1

print(count)
