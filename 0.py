nums = list(map(int,input().split()))

nums = set(nums)
nums = list(nums)
sum_nums = 0
for x in nums:
    if x>=0:
        sum_nums = sum_nums+x
        # print(x)
        # nums.remove(x)
print(sum_nums)