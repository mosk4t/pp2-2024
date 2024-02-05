def histogram(nums):
    for i in nums:
        print("*" * i)
nums = [int(el) for el in input().split()]
histogram(nums)