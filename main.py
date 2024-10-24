# Put your function here
def decreaseElements(nums):
    return [[num-1 for num in row] for row in nums]

# testing
nums = [[96, 5, 23, 16, 45, 63],[20,106,50,27,38,15]]
print(decreaseElements(nums))