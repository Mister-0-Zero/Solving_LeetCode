from typing import Optional

# Определение класса ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next

# Функция для создания связанного списка из массива
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Функция для печати связанного списка
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Создание связанного списка из массива
linked_list = create_linked_list([1, 2, 3])

# Вызов метода removeNthFromEnd
ex = Solution()
result = ex.removeNthFromEnd(linked_list, 1)

# Печать результата
print_linked_list(result)
