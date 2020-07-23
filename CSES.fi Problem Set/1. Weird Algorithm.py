n = int(input(""))

output = ""
output += str(n) + " "

while n != 1:
    if n % 2 != 0:
        n = (3*n)+1
    else:
        n = n//2
    output += str(n) + " "

print(output)
