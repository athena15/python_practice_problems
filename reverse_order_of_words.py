from typing import List

"""
Problem: Reverse Words in a String

Given a string s, reverse the order of the words. Words are separated by spaces.
Return string of words in reverse order with single spaces between words.

LeetCode: https://leetcode.com/problems/reverse-words-in-a-string/

Examples:
"the sky is blue" -> "blue is sky the"
"  hello world  " -> "world hello"
"a good   example" -> "example good a"

Input:
- s: str - string containing words separated by spaces

Output:
- str - words in reverse order, single-spaced

Note:
- Remove leading/trailing spaces
- Reduce multiple spaces to single space
- At least one word in input
- String contains letters, digits, and spaces
- 1 <= s.length <= 104

Follow-up: Can you solve it in-place with O(1) extra space?
"""


def reverseWords(s: str) -> str:
    return " ".join(s.strip().split()[::-1])


print(reverseWords("the sky is blue"))  # "blue is sky the"
print(reverseWords("  hello world  "))  # "world hello"
print(reverseWords("a good   example"))  # "example good a"
