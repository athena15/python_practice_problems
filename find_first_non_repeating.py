"""
Problem: First Non-repeating Character

Given a string, find the first character that appears exactly once (non-repeating).
Return None if no such character exists.

Example:
"leetcode" -> 'l'  (first char that appears only once)
"aabbcc" -> None   (all chars repeat)
"aabbc" -> 'c'     (both 'c' appears only once, but 'c' appears first)

Input:
- text: str - String to analyze (can be empty)

Output:
- str or None - First character that appears exactly once, or None if no such character

Note: Consider case sensitivity ('A' != 'a')
"""

from collections import Counter

def find_first_non_repeating(text: str) -> str | None:
    counter = Counter(text)
    for letter in text:
        if counter[letter] == 1:
            return letter

    return None


# Test cases
test1 = "leetcode"
test2 = "aabbcc"
test3 = "aabbc"

print(find_first_non_repeating(test1))  # Should print: 'l'
print(find_first_non_repeating(test2))  # Should print: None
print(find_first_non_repeating(test3))  # Should print: 'c'