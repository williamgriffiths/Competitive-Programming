n = int(input(""))
count = str(n).count("4") + str(n).count("7")
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
