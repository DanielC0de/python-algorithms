nums = [3, 5, 2, 4, 6, 1, 8, 7, 9]


def Selection_sort(nums):
    for i in range(len(nums)):
        lowest = i

        for j in range(i+1, len(nums)):
            if nums[j] < nums[lowest]:
                lowest = j
        nums[i], nums[lowest] = nums[lowest], nums[i]
    return nums


print("было", nums)
print("стало", Selection_sort(nums))
