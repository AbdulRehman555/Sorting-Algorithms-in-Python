def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                # swapping
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True


# Input List
nums = [5, 1, 8, 2, 7]

bubble_sort(nums)

# Sorted List
print(nums)