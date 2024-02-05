def has_33(nums):
    pass
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

nums = [int(el) for el in input().split()]
res = has_33(nums)
print(res)