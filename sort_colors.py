"""
Problem: Sort Colors (Three-Way Partition)

Given an array containing only 0s, 1s, and 2s, sort them in-place.

Examples:
[2, 0, 1, 2, 1, 0] -> [0, 0, 1, 1, 2, 2]
[1, 1, 0, 2] -> [0, 1, 1, 2]
[2, 1, 2] -> [1, 2, 2]

Input:
- nums: List[int] - array containing only 0s, 1s, and 2s

Output:
- None (modify array in-place)

Note:
- Must be done in a single pass
- Must be done in-place (no extra array)
- Elements must maintain relative order within their group
"""
from typing import List

def sort_colors(nums: List[int]) -> None:
    low = 0  # where we put the next zero - everything BEFORE this index is a 0
    mid = 0  # current element we're looking at
    high = len(nums) - 1  # where we put the next 2 - everything AFTER this index is a 2

    # Visual representation: [0s] [1s] [unsorted] [2s]

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid +=1

    return nums


sort_colors([2, 0, 1, 2, 1, 0])