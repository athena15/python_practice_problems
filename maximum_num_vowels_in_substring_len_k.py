from typing import List

"""
Problem: Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any 
substring of s with length k.

LeetCode: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Examples:
s = "abciiidef", k = 3 -> 3
Explanation: "iii" contains 3 vowels

s = "aeiou", k = 2 -> 2
Explanation: Any substring of length 2 contains 2 vowels

s = "leetcode", k = 3 -> 2
Explanation: "lee", "eet" and "ode" contain 2 vowels

Input:
- s: str - input string containing lowercase English letters
- k: int - length of substring to consider

Output:
- int - maximum number of vowels in any substring of length k

Note:
- Vowels are 'a', 'e', 'i', 'o', and 'u'
- 1 <= k <= s.length <= 105
"""


def maxVowels(s: str, k: int) -> int:
    vowels = set("aeiou")
    current_vowel_count = sum(1 for letter in s[:k] if letter in vowels)
    max_vowel_count = current_vowel_count

    for i in range(k, len(s)):
        if s[i - k] in vowels:
            current_vowel_count -= 1

        if s[k] in vowels:
            current_vowel_count += 1

        max_vowel_count = max(current_vowel_count, max_vowel_count)

    return max_vowel_count


print(maxVowels("abciiidef", 3))  # 3
print(maxVowels("aeiou", 2))  # 2
print(maxVowels("leetcode", 3))  # 2
