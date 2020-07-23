n = int(input())
lst = []
amazing = 0

scores = input()
scores = list(map(int, scores.split()))

for i in range(n):
    score = scores[i]

    if len(lst) > 0:
        if score > max(lst) or score < min(lst):
            amazing += 1
        
    lst.append(score)

print(amazing)

