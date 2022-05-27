"""
    Quick Sort Algorithm Implementation with selecting last element as pivot. 
"""


def quick_sort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()

    items_greater = []
    items_lower = []

    for item in nums:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# Input List
nums = [5, 1, 8, 2, 7]

print(quick_sort(nums))