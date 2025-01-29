from typing import List

"""
Problem: Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, check if concatenating each array's strings gives the same result.

LeetCode: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Examples:
word1 = ["ab", "c"], word2 = ["a", "bc"] -> True ("abc" == "abc")
word1 = ["a", "cb"], word2 = ["ab", "c"] -> False ("acb" != "abc")
word1 = ["abc", "d", "defg"], word2 = ["abcddefg"] -> True

Input:
- word1: List[str] - first array of strings
- word2: List[str] - second array of strings

Output:
- bool - True if concatenated strings are equal
"""

def array_strings_are_equal(word1: List[str], word2: List[str]) -> bool:
    return ''.join(word1) == ''.join(word2)

print(array_strings_are_equal(["ab", "c"], ["a", "bc"]))  # True
print(array_strings_are_equal(["a", "cb"], ["ab", "c"]))  # False
print(array_strings_are_equal(["abc", "d", "defg"], ["abcddefg"]))  # True