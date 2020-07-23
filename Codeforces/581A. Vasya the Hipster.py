ab = input()
a,b = (int(i) for i in ab.split())

pairs = min(a,b)
odd = (a+b)//2 - pairs
print(pairs,odd)
