from typing import List

"""
Problem: Jump Game

Given array nums, initially at position 0, each element represents max jump length at 
that position. Determine if you can reach last index.

LeetCode: https://leetcode.com/problems/jump-game/

Examples:
[2,3,1,1,4] -> True (Jump 1 to index 1, then 3 to last index)
[3,2,1,0,4] -> False (Can't get past index 3)
[0] -> True

Input:
- nums: List[int] - array of non-negative integers
Output:
- bool - True if last index is reachable
"""


def can_jump(nums: List[int]) -> bool:
    furthest = 0

    for i in range(len(nums)):
        if i > furthest:
            return False

        furthest = max(furthest, i + nums[i])

        if furthest >= len(nums) - 1:
            return True

    return True


print(can_jump([2, 3, 1, 1, 4]))  # True
print(can_jump([3, 2, 1, 0, 4]))  # False
print(can_jump([0]))  # True
