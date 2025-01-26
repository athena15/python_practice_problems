from typing import List

"""
Problem: Sort Colors (Dutch National Flag)

Given array with objects colored red, white, or blue (represented as 0, 1, and 2), 
sort them in-place so objects of same color are adjacent.

LeetCode: https://leetcode.com/problems/sort-colors/

Examples:
[2,0,2,1,1,0] -> [0,0,1,1,2,2]
[2,0,1] -> [0,1,2]
[0] -> [0]

Input:
- nums: List[int] - array where elements are 0, 1, or 2

Output:
- None (modify nums in-place)
"""


def sort_colors(nums: List[int]) -> None:

    left = 0
    mid = 0
    right = len(nums) - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 2:
            nums[right], nums[mid] = nums[mid], nums[right]
            right -= 1

        else:
            mid += 1


test1 = [2, 0, 2, 1, 1, 0]
test2 = [2, 0, 1]
test3 = [0]

sort_colors(test1)
print(test1)  # [0,0,1,1,2,2]
sort_colors(test2)
print(test2)  # [0,1,2]
sort_colors(test3)
print(test3)  # [0]
