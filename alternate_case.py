"""
Problem: Alternate Case

Write a function that converts a string so that characters alternate between uppercase and lowercase.
Start with uppercase.

Examples:
"hello" -> "HeLlO"
"python" -> "PyThOn"
"WORLD" -> "WoRlD"
"a" -> "A"

Input:
- text: str - any string

Output:
- str - string with alternating case

Note:
- Empty string returns empty string
- Spaces and special characters don't affect the alternation but stay unchanged
"""

def alternate_case(text: str) -> str:
    if text == "":
        return ""

    count = 0
    solution = []
    for char in text:
        if not char.isalpha():
            solution.append(char)
        else:
            if count % 2 == 0:
                solution.append(char.upper())
            else:
                solution.append(char.lower())
            count += 1
    return "".join(solution)


print(alternate_case("hello0 world"))