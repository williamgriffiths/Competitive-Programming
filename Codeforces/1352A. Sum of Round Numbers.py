t = int(input())

for i in range(t):
    n = int(input())
    s = 0
    nums = []

    s = len(str(n)) - str(n).count("0") 
    print(s)

    for num in list(str(n))[::-1]:
        if num != "0":
            nums.append(int(num)*10**list(str(n))[::-1].index(num))
            n -= int(num)*10**list(str(n))[::-1].index(num)
            #nums.append(n)
            
    print(" ".join(str(x) for x in nums[::-1]))
