n = int(input(""))
cap = 0
capMax = 0

for i in range(n):
    offOn = input("")
    offOn = list(map(int, offOn.split()))
    off,on = offOn[0], offOn[1]

    cap -= off
    cap += on
    if capMax < cap:
        capMax = cap

print(capMax)

    
