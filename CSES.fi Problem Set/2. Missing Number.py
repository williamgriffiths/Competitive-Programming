n = int(input(""))
numbers = input("")

nums = [int(num) for num in numbers.split()]
print(sum(range(1,n+1)) - sum(nums))
