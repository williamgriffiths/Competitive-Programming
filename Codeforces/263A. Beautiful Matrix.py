row = 0
col = 0

for i in range(5):
    matrix = input("")
    if "1" in matrix:
        row = i
        col = matrix.replace(" ","").index("1") % 5

moves = abs(row-2)+abs(col-2)
print(moves)
