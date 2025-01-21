from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return head.next

def createLinkedList(list_val):

    if not list_val:
        return None

    head = ListNode(list_val[0])
    current = head

    for val in list_val[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def printList(list_node):

    while list_node:
        print(f'{list_node.val} -> ', end = '')
        list_node = list_node.next
    print("None")

list1 = createLinkedList([1, 2, 2, 4, 5, 5, 7])
printList(list1)

list2 = createLinkedList([0, 1, 3, 4, 5, 5, 8])
printList(list2)

instance = Solution()
printList(instance.mergeTwoLists(list1, list2))


