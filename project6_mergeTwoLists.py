# 주어진 두 개의 정렬된 연결 리스트를 하나의 정렬된 연결 리스트로 병합하는 기능을 합니다.
# This function merges two sorted linked lists into one sorted linked list.
#
# Args:
#     list1 (ListNode): 첫 번째 정렬된 연결 리스트의 헤드 노드입니다. (Head of the first sorted linked list)
#     list2 (ListNode): 두 번째 정렬된 연결 리스트의 헤드 노드입니다. (Head of the second sorted linked list)
#
# Returns:
#     ListNode: 병합된 정렬된 연결 리스트의 헤드 노드를 반환합니다. (Returns the head of the merged sorted linked list)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 더미 노드를 사용하여 결과 리스트의 시작을 추적합니다.
        # Use a dummy node to keep track of the start of the result list
        dummy = ListNode()
        current = dummy

        # 두 리스트의 모든 요소를 순회합니다.
        # Traverse both lists until at least one of them is empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # 다음 노드로 진행합니다.
            # Move to the next node in the result list
            current = current.next

        # 남아 있는 노드를 결과 리스트에 추가합니다.
        # Attach the remaining nodes, if any, from either list1 or list2
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # 더미 노드의 다음 노드가 병합된 결과 리스트의 시작입니다.
        # Return the merged list, which starts after the dummy node
        return dummy.next

# 테스트 예시
# Example usage
def print_list(node: ListNode):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)

# 예제 리스트를 만듭니다.
# Creating example lists
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Solution 클래스의 인스턴스를 생성하고 병합합니다.
# Creating an instance of Solution and merging lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# 병합된 리스트를 출력합니다.
# Printing the merged list
print_list(merged_list)  # Output: [1, 1, 2, 3, 4, 4]
