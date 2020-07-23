y = int(input(""))

if len(set(str(y))) == len(str(y)):
    y += 1
    
while len(set(str(y))) != len(str(y)):
    y += 1
    
print(y)
