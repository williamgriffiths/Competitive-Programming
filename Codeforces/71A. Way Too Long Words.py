n = int(input(""))
output = []

for i in range(n):
    word = input("")
    if len(word) <= 10:
        output.append(word)
    elif 10 < len(word) <= 100:
        output.append(word[0]+str(len(word)-2)+word[len(word)-1])

print("\n".join(output))

