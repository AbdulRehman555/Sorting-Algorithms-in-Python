def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        #swapping
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

# Input List
nums = [5, 1, 8, 2, 7]

selection_sort(nums)

# Sorted List
print(nums)