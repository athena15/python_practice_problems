from typing import List

"""
Problem: Kids With the Greatest Number of Candies

Given array of candy counts and number of extra candies, determine if giving all extra 
candies to each kid would give them the most candies among all kids.

LeetCode: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Examples:
[2,3,5,1,3], extraCandies = 3 -> [true,true,true,false,true]
[4,2,1,1,2], extraCandies = 1 -> [true,false,false,false,false]
[12,1,12], extraCandies = 10 -> [true,false,true]

Input:
- candies: List[int] - array where candies[i] is number of candies kid i has
- extraCandies: int - number of extra candies to give

Output:
- List[bool] - whether each kid could have the most candies

Note:
- Multiple kids can have the greatest number of candies
- n == candies.length
- 2 <= n <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50
"""


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    result = []
    for candy in candies:
        result.append(candy + extraCandies >= max(candies))

    return result


print(kidsWithCandies([2, 3, 5, 1, 3], 3))  # [True,True,True,False,True]
print(kidsWithCandies([4, 2, 1, 1, 2], 1))  # [True,False,False,False,False]
print(kidsWithCandies([12, 1, 12], 10))  # [True,False,True]
