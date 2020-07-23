n = int(input())
hs = input()
hs = list(map(int, hs.split()))
swaps = 0

maxIndex = hs.index(max(hs))
minIndex = hs.index(min(hs))

if hs[0] != max(hs):
    print(hs[maxIndex],hs[maxIndex-1])
    hs[maxIndex],hs[maxIndex-1] = hs[maxIndex-1],hs[maxIndex]
    print(hs[maxIndex],hs[maxIndex-1])
    swaps += 1

if hs[n-1] != min(hs):
    print(hs[minIndex],hs[minIndex+1])
    hs[minIndex],hs[minIndex+1] = hs[minIndex+1],hs[minIndex]
    print(hs[minIndex],hs[minIndex+1])
    swaps += 1

        
print(swaps)
