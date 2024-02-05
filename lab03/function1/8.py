def spy_game(nums):
    pass 
    for i in nums:
        if nums[i] == 0 and nums[i+1] == 0 and nums[i+2]==7:
            return True
        else:
            return False

nums = [int(el) for el in input().split()]
print(spy_game(nums))