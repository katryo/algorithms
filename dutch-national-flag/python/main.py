# https://en.wikipedia.org/wiki/Dutch_national_flag_problem


def divide(nums, mid_val):
    left = 0
    middle = 0
    right = len(nums)-1

    while middle <= right:
        if nums[middle] > mid_val:
            nums[middle], nums[right] = nums[right], nums[middle]
            right -= 1
        elif nums[middle] == mid_val:
            middle += 1
        else:  # nums[middle] < mid_val:
            nums[left], nums[middle] = nums[middle], nums[left]
            left += 1
            middle += 1
    return nums


print(divide([1,3,2,3,1,3,2,2,3,3,1,2,1], 2))

