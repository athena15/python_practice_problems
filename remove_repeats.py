"""
Problem: Remove Repeats

Write a function that takes a list of numbers and returns a new list where 
any consecutive repeated numbers are reduced to a single number.

Examples:
[1, 1, 2, 2, 3] -> [1, 2, 3]
[1, 2, 2, 3, 3, 3, 4] -> [1, 2, 3, 4]
[1] -> [1]
[] -> []
[1, 1, 1, 2, 1] -> [1, 2, 1]  # Note: 1 appears twice because they're not consecutive

Input:
- nums: List[int] - list of integers

Output:
- List[int] - list with consecutive duplicates removed

Note:
- Order should be preserved
- Only remove consecutive duplicates
- Return new list (don't modify original)
"""
from typing import List

def remove_consecutive_duplicates(nums: List[int]) -> List[int]:
    if not nums:
        return []

    solution = []
    current_char = nums[0]

    solution.append(current_char)

    for i, v in enumerate(nums, start=1):
        if current_char == v:
            continue
        else:
            solution.append(v)
            current_char = v

    return solution


print(remove_consecutive_duplicates([1, 2, 2, 3, 3, 3, 4]))  # returns [1, 2, 3, 4]


