dct = input()
lst = []

for char in dct:
    if char.isalpha():
        lst.append(char)

print(len(set(lst)))
