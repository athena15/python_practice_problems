from typing import List

"""
Problem: Is Subsequence

Given two strings s and t, determine if s is a subsequence of t. A subsequence is a 
string that can be derived from another string by deleting some or no elements without 
changing the order of the remaining elements.

LeetCode: https://leetcode.com/problems/is-subsequence/

Examples:
s = "abc", t = "ahbgdc" -> True
s = "axc", t = "ahbgdc" -> False
s = "", t = "ahbgdc" -> True

Input:
- s: str - string to check if it's a subsequence
- t: str - string to check against

Output:
- bool - True if s is a subsequence of t, False otherwise

Note:
- Empty string is a subsequence of any string
- Order matters
- Characters don't need to be consecutive in t
"""


def isSubsequence(s: str, t: str) -> bool:
    left = 0
    right = 0

    while right < len(t):
        if left == len(s):
            return True

        if s[left] == t[right]:
            left += 1
            right += 1
        else:
            right += 1

    if left == len(s):
        return True

    return False


print(isSubsequence("abc", "ahbgdc"))  # True
print(isSubsequence("axc", "ahbgdc"))  # False
print(isSubsequence("", "ahbgdc"))  # True
