n = int(input(""))
count = 0

for i in range(n):
    nums = input("")
    if nums.count("1") > nums.count("0"):
        count += 1

print(count)
