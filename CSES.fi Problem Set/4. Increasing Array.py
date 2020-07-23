n = int(input())
nums = input()
nums = [int(i) for i in nums.split()]
count = 0

for i in range(n-1):
    if nums[i] > nums[i+1]:
        count += nums[i] - nums[i+1]
        nums[i+1] = nums[i]

print(count)
