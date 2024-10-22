"""
주어진 문자열에서 괄호가 유효한지 여부를 판단하는 기능을 합니다.
(This function determines if the input string has valid brackets.)

Args:
    s (str): 괄호 유효성을 검사할 문자열입니다. (String to check for bracket validity)

Returns:
    bool: 문자열의 괄호가 유효하다면 True, 그렇지 않다면 False를 반환합니다. (Returns True if the brackets are valid, otherwise False)
"""

def isValid(s: str) -> bool:
    # Create a stack to keep track of opening brackets
    # 여는 괄호들을 추적하기 위한 스택을 생성합니다.
    stack = []
    # Define a mapping of closing to opening brackets
    # 닫는 괄호와 여는 괄호의 매핑을 정의합니다.
    mapping = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the string
    # 문자열의 각 문자를 순회합니다.
    for char in s:
        # If the character is a closing bracket
        # 문자가 닫는 괄호라면
        if char in mapping:
            # Pop the top element from the stack if it is not empty, otherwise assign a dummy value
            # 스택이 비어있지 않으면 스택의 맨 위 요소를 꺼내고, 그렇지 않으면 임시 값을 할당합니다.
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            # 꺼낸 요소가 해당 여는 괄호와 일치하는지 확인합니다.
            if mapping[char] != top_element:
                return False
        else:
            # If it is an opening bracket, push it onto the stack
            # 여는 괄호라면 스택에 추가합니다.
            stack.append(char)
    
    # If the stack is empty, all brackets were properly closed
    # 스택이 비어 있다면 모든 괄호가 올바르게 닫힌 것입니다.
    return not stack

# Example usage
# 사용 예시
print(isValid("()"))       # Output: True
print(isValid("()[]{}"))   # Output: True
print(isValid("(]"))       # Output: False
print(isValid("([])"))     # Output: True
