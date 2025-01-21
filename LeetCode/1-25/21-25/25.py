from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head and not head.next: return head

        head_ = ListNode(0, head)
        prev = head_
        current = head

        def check(current):
            if current:
                for i in range(k - 1):
                    if current.next: current = current.next
                    else: return False
                return True

        while check(current):

            mass_link_list = [current]

            for i in range(k - 1):
                mass_link_list.append(current.next)
                current = current.next

            prev.next = mass_link_list[k - 1]
            mass_link_list[0].next = mass_link_list[k - 1].next

            for i in range(k - 1, 0, -1):
                mass_link_list[i].next = mass_link_list[i - 1]

            prev = mass_link_list[0]
            for i in range(k):
                current = current.next

        return head_.next

instance = Solution()

def print_(head):
    mass = []
    while head:
        mass.append(head.val)
        head = head.next
    print(" -> ".join(map(str, mass)))

list_ = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print_(instance.reverseKGroup(list_, 2))

list_ = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print_(instance.reverseKGroup(list_, 3))

list_ = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print_(instance.reverseKGroup(list_, 4))