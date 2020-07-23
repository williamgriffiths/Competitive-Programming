dna = input("")
ans = 1
length = 0

currentChar = "A"

for char in dna:
    if char == currentChar:
        length += 1
        ans = max(ans, length)

    else:
        currentChar = char
        length = 1

print(ans)
