"""
Problem: Minimum Sum Subarray

Given an array of integers and a window size k, find the minimum sum of any 
contiguous subarray of size k.

Examples:
[2, 1, 3, -4, 5, 2, 1], k=3 -> 0  (subarray [-4, 5, 2])
[1, 1, 1, 1, 1], k=2 -> 2  (any subarray works as they're all sum to 2)
[5, 2, -1, 0, 3], k=3 -> 1  (subarray [-1, 0, 3])
[4], k=1 -> 4

Input:
- nums: List[int] - array of integers
- k: int - size of subarray to consider

Output:
- int - minimum sum found in any subarray of size k

Note:
- k will always be valid (1 ≤ k ≤ length of array)
- Array can contain negative numbers
- Return 0 if nums is empty
"""

from typing import List

def min_sum_subarray(nums: List[int], k: int) -> int:
    if not nums:
        return 0

    window_sum = sum(nums[:k])
    min_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        min_sum = min(min_sum, window_sum)
        min_sum = min(window_sum, min_sum)

    return min_sum




print(min_sum_subarray(nums = [1, 3, -1, -3, 5, 3, -4, -2], k = 3))  # -3