from typing import List

"""
Problem: Find Numbers with Even Number of Digits

Given an array of integers, return count of numbers that have an even number of digits.

LeetCode: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Examples:
[12,345,2,6,7896] -> 2 (12 and 7896 have even number of digits)
[555,901,482,1771] -> 1 (only 482 has even number of digits)

Input:
- nums: List[int] - array of positive integers

Output:
- int - count of numbers with even number of digits
"""


def find_numbers(nums: List[int]) -> int:
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1

    return count

    # # or with generator comprehension (fancy!):
    # return sum(len(str(num)) % 2 == 0 for num in nums)


print(find_numbers([12, 345, 2, 6, 7896]))  # 2
print(find_numbers([555, 901, 482, 1771]))  # 1
print(find_numbers([1, 2, 3, 4]))  # 0
