n = int(input())

px = input()
p,x = (int(i) for i in px.split())

y = input()
y = list(map(int, y.split()))
y = y[1:]

x.extend(y)

if 0 in x:
    x.remove(0)
    
nums = [i for i in range(1,n+1)]

if len(set(x)) == len(nums):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
