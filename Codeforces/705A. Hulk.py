n = int(input(""))
output = ""

while n > 2:
    output += "I hate that I love that "
    n -= 2

if n % 2 == 0 and n > 0:
    output += "I hate that I love it"
if n % 2 != 0:
    output += "I hate it"

print(output)
