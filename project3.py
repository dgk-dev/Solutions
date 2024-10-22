"""
주어진 로마 숫자 문자열을 정수로 변환하는 기능을 합니다..
(This function converts a given Roman numeral string to an integer.)

Args:
    s (str): 변환할 로마 숫자 문자열입니다. (Roman numeral string to convert)

Returns:
    int: 변환된 정수 값을 반환합니다. (Returns the converted integer value)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        txt_length = len(s)
        
        # 로마 숫자를 왼쪽에서 오른쪽으로 순회합니다. (Iterate through the Roman numeral from left to right)
        for i in range(txt_length):
            # 현재 숫자가 다음 숫자보다 작다면 빼기 연산을 수행합니다. (If the current number is smaller than the next, subtract it)
            if i < txt_length - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                total -= roman_dict[s[i]]
            else:
                total += roman_dict[s[i]]
        
        return total

# 결과 출력 (Print result)
result = Solution().romanToInt("IIIIV")
print(result)
