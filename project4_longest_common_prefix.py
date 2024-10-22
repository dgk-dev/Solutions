"""
주어진 문자열 배열에서 가장 긴 공통 접두사를 찾는 기능을 합니다.
(This function finds the longest common prefix string amongst an array of strings.)

Args:
    strs (List[str]): 공통 접두사를 찾을 문자열 리스트입니다. (List of strings to find the common prefix)

Returns:
    str: 가장 긴 공통 접두사를 반환합니다. 공통 접두사가 없을 경우 빈 문자열을 반환합니다. (Returns the longest common prefix or an empty string if none is found)
"""

def longest_common_prefix(strs):
    # 입력 리스트가 비어 있는지 확인합니다. 비어 있다면 빈 문자열을 반환합니다.
    # Check if the input list is empty. If so, return an empty string.
    if not strs:
        return ""
    
    # 리스트의 첫 번째 문자열로 접두사를 초기화합니다.
    # Initialize the prefix with the first string in the list.
    prefix = strs[0]
    
    # 리스트의 나머지 문자열들을 순회합니다.
    # Iterate over the remaining strings in the list.
    for i in range(1, len(strs)):
        # 현재 문자열의 시작과 접두사가 일치할 때까지 접두사를 줄입니다.
        # Continuously shorten the prefix until it matches the start of the current string.
        while strs[i].find(prefix) != 0:
            # 접두사의 마지막 문자를 제거합니다.
            # Remove the last character from the prefix.
            prefix = prefix[:-1]
            # 접두사가 빈 문자열이 되면 공통 접두사가 없으므로 빈 문자열을 반환합니다.
            # If the prefix becomes empty, there is no common prefix, so return an empty string.
            if not prefix:
                return ""
    
    # 모든 문자열을 비교한 후 최종 접두사를 반환합니다.
    # Return the final common prefix after comparing all strings.
    return prefix

# 사용 예시
# Example Usage
strs1 = ["flower", "flow", "flight"]
print(longest_common_prefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(longest_common_prefix(strs2))  # Output: ""
