from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return None
        if not head.next: return head

        head_ = ListNode(0, head)
        prev = head_
        current = head

        while current and current.next:
            first = current
            second = current.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            current = first.next

        return head_.next

instance = Solution()

def print_(head):
    mass = []
    while head:
        mass.append(head.val)
        head = head.next
    print(" -> ".join(map(str, mass)))

print_(instance.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))