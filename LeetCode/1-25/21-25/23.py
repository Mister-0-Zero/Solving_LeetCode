from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:

        mass_value = []

        for list_ in lists:
            while list_:
                mass_value.append(list_.val)
                list_ = list_.next

        if not mass_value: return None

        mass_value.sort()

        head = ListNode(mass_value[0])
        current = head

        for value in mass_value[1:]:
            new_node = ListNode(value)
            current.next = new_node
            current = current.next

        return head


def createLML(mass_value):
    head = ListNode(mass_value[0])
    current = head

    for value in mass_value[1:]:
        new_node = ListNode(value)
        current.next = new_node
        current = current.next

    return head

def print_(mass):
    output = []
    current = mass
    while current:
        output += [str(current.val)]
        current = current.next
    return " -> ".join(output)

# instance1 = createLML([2, 4])
# print_(instance1)
# instance2 = createLML([1, 2, 5])
# print_(instance2)
# instance3 = createLML([1, 1, 3, 4, 8])
# print_(instance3)
#
# mass = [instance3, instance2]

lists = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6))
]

instance = Solution()
merged_list = instance.mergeKLists(lists)

# Print the merged list
current = merged_list
result = []
while current:
    result.append(current.val)
    current = current.next
print(" -> ".join(map(str, result)))