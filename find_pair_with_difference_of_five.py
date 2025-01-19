

from typing import List, Tuple, Optional

def find_pair_with_difference(target_diff: int, numbers: List) -> Optional[Tuple]:
    if not numbers:
        return None

    left = 0
    right = 1

    while right < len(numbers):
        current_diff = numbers[right] - numbers[left]
        if current_diff == target_diff:
            print(f"Found match!")
            return (numbers[left], numbers[right])
        elif current_diff > target_diff:
            print(f"Current diff > 5: {current_diff}")
            print("Moving left pointer. If right and left are the same, moving right pointer")
            left += 1
            if left == right:
                right += 1
        elif current_diff < target_diff:
            print(f"Current diff < 5: {current_diff}")
            print("Moving right pointer")
            right +=1

    return None


TARGET_DIFF = 5
numbers = [1, 3, 7, 8, 11, 13]
numbers2 = [1, 4, 8, 9, 10, 11]
print(find_pair_with_difference(TARGET_DIFF, numbers2))