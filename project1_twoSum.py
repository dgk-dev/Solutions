"""
이 프로그램은 주어진 리스트에서 두 숫자의 합이 특정 타겟 값과 일치하는 인덱스를 찾는 기능을 합니다. 
(This program finds the indices of two numbers in a given list that add up to a specific target value.)

Args:
    nums (List[int]): 숫자의 리스트입니다. (List of numbers)
    target (int): 목표 합계 값입니다. (Target value)

Returns:
    List[int]: 두 숫자의 인덱스를 포함하는 리스트를 반환합니다. (Returns a list containing the indices of the two numbers)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 사용 예시
# Example Usage
nums1 = [2, 7, 11, 15]
target1 = 9
print(Solution().twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(Solution().twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(Solution().twoSum(nums3, target3))  # Output: [0, 1]