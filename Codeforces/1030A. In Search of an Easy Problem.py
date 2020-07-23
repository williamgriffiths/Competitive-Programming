n = int(input(""))
nums = input("")
nums = list(map(int, nums.split()))

if nums.count(1) != 0:
    print("HARD")
else:
    print("EASY")
