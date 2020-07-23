nm = input()
n,m = (int(i) for i in nm.split())

for i in range(1,n+1):
    Nif i % 2 != 0:
        print("#"*m)
    elif i % 4 == 0:
        print("#"+"."*(m-1))
    else:
        print("."*(m-1)+"#")
