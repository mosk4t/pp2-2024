import random

def histogram(nums):
    for i in nums:
        print("*" * i)

x = int(input("Write a number of elements of list:"))
nums = []
for i in range(x+1):
    s = random.randint(1, 15)
    nums.append(s)
histogram(nums)
