from typing import List

# 주어진 배열에서 특정 값을 제거하고 나머지 요소들을 인-플레이스(in-place)로 유지합니다.
# This function removes all occurrences of a given value from an array in-place.
#
# Args:
#     nums (List[int]): 제거할 값을 포함할 수 있는 정수 배열입니다. (List of integers which may contain the value to remove)
#     val (int): 제거할 값입니다. (Value to remove)
#
# Returns:
#     int: 제거된 후 남아있는 요소의 개수를 반환합니다. (Returns the number of remaining elements after removal)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 특정 값과 같지 않은 요소들의 위치를 추적하기 위한 포인터를 초기화합니다.
        # Initialize a pointer for the position of elements not equal to val
        k = 0
        
        # 배열을 순회합니다.
        # Iterate over the array
        for i in range(len(nums)):
            # 현재 요소가 제거할 값과 다를 경우
            # If the current element is not equal to val
            if nums[i] != val:
                # 현재 요소를 포인터 k 위치에 할당합니다.
                # Assign the current element to the position k
                nums[k] = nums[i]
                # 포인터 k를 증가시킵니다.
                # Increment the pointer k
                k += 1
        
        # 특정 값을 제외한 요소의 개수를 반환합니다.
        # Return the number of elements not equal to val
        return k

# 사용 예시 1
# Example 1
solution = Solution()
nums = [3, 2, 2, 3]
val = 3
k = solution.removeElement(nums, val)
print(k)  # 출력: 2 (Output: 2)
print(nums[:k])  # 출력: [2, 2] (Output: [2, 2])

# 사용 예시 2
# Example 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = solution.removeElement(nums, val)
print(k)  # 출력: 5 (Output: 5)
print(nums[:k])  # 출력: [0, 1, 3, 0, 4] (Output: [0, 1, 3, 0, 4])
