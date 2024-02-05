def unique(nums):
    unique_list = []
    for i in nums:
            if i not in unique_list:
                unique_list.append(i)
    return unique_list
nums = [int(el) for el in input().split()]
print(unique(nums))