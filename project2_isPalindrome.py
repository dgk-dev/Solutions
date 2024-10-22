"""
주어진 정수가 팰린드롬인지 확인하는 기능을 합니다.
(This function checks if the given integer is a palindrome.)

Args:
    x (int): 확인할 정수입니다. (Integer to check)

Returns:
    bool: 정수가 팰린드롬이면 True, 그렇지 않으면 False를 반환합니다. 
    (Returns True if the integer is a palindrome, otherwise False)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 음수는 팰린드롬이 될 수 없음 (Negative numbers cannot be palindromes)
        if x < 0:
            return False
        
        # 정수를 문자열로 변환한 후, 거꾸로 뒤집어서 비교 (Convert the integer to a string and compare with its reverse)
        str_x = str(x)  
        
        # 문자열이 거꾸로 읽었을 때도 같은지 확인 (Check if the string reads the same forwards and backwards)
        return str_x == str_x[::-1]

# Example Usage
num1 = 121
print(Solution().isPalindrome(num1))  # Output: True

num2 = -121
print(Solution().isPalindrome(num2))  # Output: False

num3 = 10
print(Solution().isPalindrome(num3))  # Output: False

num4 = 12321
print(Solution().isPalindrome(num4))  # Output: True