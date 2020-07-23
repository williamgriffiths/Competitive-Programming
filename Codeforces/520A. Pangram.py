n = int(input())
s = input()
lst = [i for i in s.lower()]

if s.isalpha() and len(set(lst)) == 26:
    print("YES")
else:
    print("NO")
