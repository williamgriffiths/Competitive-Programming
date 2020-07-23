s = input("")
s = s.split("+")
s = sorted(list(map(int, s)))
print("+".join(list(map(str, s))))
