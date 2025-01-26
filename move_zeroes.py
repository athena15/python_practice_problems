"""
Problem: Move Zeroes

Given an array of numbers, move all zeroes to the end while maintaining the relative order
of non-zero elements. Do this in-place.

LeetCode: https://leetcode.com/problems/move-zeroes/

Examples:
[0,1,0,3,12] -> [1,3,12,0,0]
[0] -> [0]
[1,2,3] -> [1,2,3]

Input:
- nums: List[int] - array of integers

Output:
- None (modify nums in-place)
"""
from os import write
from typing import List

def move_zeroes(nums: List[int]) -> None:
   if not nums:
       return None

   write_pos = 0
   for read_pos in range(len(nums)):
       if nums[read_pos] == 0:
           continue
       else:
           nums[write_pos] = nums[read_pos]
           write_pos += 1

   for i in range(write_pos, len(nums)):
       nums[i] = 0

   print(nums)
   return None



test1 = [0,1,0,3,12,0,1,5,0]
test2 = [0]
test3 = [1,2,3]

move_zeroes(test1)
print(test1)  # [1,3,12,0,0]
move_zeroes(test2)
print(test2)  # [0]
move_zeroes(test3)
print(test3)  # [1,2,3]