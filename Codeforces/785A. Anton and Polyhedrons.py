n = int(input())
ans = 0

dct = {"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}

for i in range(n):
    s = input()
    ans += dct[s]

print(ans)
    
