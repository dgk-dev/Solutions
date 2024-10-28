# 주어진 정렬된 정수 배열에서 중복된 요소를 제거하고 고유한 요소만 남깁니다.
# This function removes duplicates from a sorted integer array in-place.
#
# Args:
#     nums (List[int]): 중복을 제거할 정렬된 정수 배열입니다. (Sorted integer array to remove duplicates from)
#
# Returns:
#     int: 고유한 요소의 수를 반환합니다. (Returns the number of unique elements)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # 유일한 요소를 추적하기 위한 포인터입니다.
        # Pointer to track the position of unique elements
        i = 0
        for j in range(1, len(nums)):
            # 현재 요소가 이전 요소와 다르면, 다음 위치에 복사합니다.
            # If the current element is different from the previous, copy it to the next position
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # 고유한 요소의 개수를 반환합니다.
        # Return the count of unique elements
        return i + 1

# Example usage:
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print(k)  # 출력: 5 (고유한 요소의 수)
    print(nums[:k])  # 출력: [0, 1, 2, 3, 4]
