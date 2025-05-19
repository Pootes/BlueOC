#Task2
from typing import List

def sum_top_two(nums: List[int]) -> int:
    if len(nums) < 2:
        raise ValueError("At least two integers are required")
    nums_sorted = sorted(nums, reverse=True)
    return nums_sorted[0] , nums_sorted[1] , nums_sorted[0] + nums_sorted[1]

# Example test cases
if __name__ == "__main__":
    print(sum_top_two([1, 4, 2, 3, 5]))  # 9
    print(sum_top_two([10, 15, 3]))     # 25
    print(sum_top_two([-1, -5, -3]))    # -4