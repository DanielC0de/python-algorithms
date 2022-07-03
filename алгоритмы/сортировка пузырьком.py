nums = [5, 3, 1, 2, 7, 6, 9, 8, 4]

print(nums)

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

print("Или же более легкий способ:")
nums = [5, 3, 1, 2, 7, 6, 9, 8, 4]

print(nums)

swaps = True
while swaps:
    swaps = False
    for j in range(len(nums)-1):
        if nums[j] > nums[j+1]:
            swaps = True
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)
