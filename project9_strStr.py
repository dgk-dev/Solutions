# 이 함수는 'haystack'에서 'needle'이 처음 발생하는 인덱스를 찾습니다.
# 'needle'이 'haystack'의 일부가 아닌 경우 -1을 반환합니다.
#
# Args:
#     haystack (str): 검색할 메인 문자열입니다. (The main string in which we are searching)
#     needle (str): 찾고자 하는 부분 문자열입니다. (The substring that we want to find)
#
# Returns:
#     int: 'needle'이 'haystack'에서 처음 발생하는 인덱스를 반환하거나, 'needle'이 없으면 -1을 반환합니다. (Returns the index of the first occurrence of 'needle' in 'haystack', or -1 if 'needle' is not found)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # needle이 비어 있는지 확인하고, 비어 있으면 0을 반환합니다. (Check if needle is empty, if yes, return 0)
        if not needle:
            return 0

        # haystack과 needle의 길이를 가져옵니다. (Get the lengths of haystack and needle)
        haystack_length = len(haystack)
        needle_length = len(needle)

        # haystack을 순회하며 범위를 초과하지 않도록 합니다. (Iterate through haystack, ensuring we do not go out of bounds)
        for i in range(haystack_length - needle_length + 1):
            # 부분 문자열이 needle과 일치하는지 확인합니다. (Check if the substring matches needle)
            if haystack[i:i + needle_length] == needle:
                return i

        # 일치하는 것이 없으면 -1을 반환합니다. (If no occurrence was found, return -1)
        return -1
