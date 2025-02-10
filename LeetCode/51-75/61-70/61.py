from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        mass_val = self.find_value(head)
        k = k % len(mass_val)
        res_ = mass_val[-k:] + mass_val[:-k]
        head_res = ListNode(res_[0])
        current_res = head_res
        for val in res_[1:]:
            current_res.next = ListNode(val)
            current_res = current_res.next

        return head_res

    def find_value(self, head):
        current = head
        mass_val = [current.val]
        while current.next:
            current = current.next
            mass_val.append(current.val)
        return mass_val

def print_LL(head):
    current = head
    while current.next:
        print(f" {current.val} -> ", end = "")
        current = current.next
    print(f" {current.val}")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
instance = Solution()
res = instance.rotateRight(head, 2)
print_LL(res)