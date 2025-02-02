"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""


def merge_alternately(word1: str, word2: str) -> str:
    result = ""
    for a, b in zip(word1, word2):
        result += a + b  # appending to list, rather than concatenating, can be a bit more efficient
    return result + word1[len(word2):] + word2[len(word1):]


print(merge_alternately("abcd", "pq"))  # returns "apbqcd"
