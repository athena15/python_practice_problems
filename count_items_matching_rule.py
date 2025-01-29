from typing import List

"""
Problem: Count Items Matching a Rule

Given an array items where items[i] = [type, color, name] and a rule consisting of two strings: 
ruleKey and ruleValue, count number of items matching rule.

LeetCode: https://leetcode.com/problems/count-items-matching-a-rule/

Examples:
items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
-> 1 (only the lenovo matches)

Input:
- items: List[List[str]] - list of items where each item has [type, color, name]
- ruleKey: str - either "type", "color", or "name"
- ruleValue: str - value to match

Output:
- int - count of items matching the rule
"""


def count_matches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    rule_mapping = {"type": 0, "color": 1, "name": 2}
    count = 0

    for item in items:
        if item[rule_mapping[ruleKey]] == ruleValue:
            count += 1

    return count

# Test cases
items1 = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
print(count_matches(items1, "color", "silver"))  # 1
print(count_matches(items1, "type", "phone"))  # 2
print(count_matches(items1, "name", "pixel"))  # 1
