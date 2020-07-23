n = int(input())

def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            prime = False
            break
        else:
            prime = True

    return prime

for i in range(n//2,3,-1):
    if isPrime(i) == False and isPrime(n-i) == False:
        print(i,n-i)
        break
