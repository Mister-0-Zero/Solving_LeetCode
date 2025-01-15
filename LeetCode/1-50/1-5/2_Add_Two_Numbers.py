# Определение класса ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Определение класса Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2
        s1 = ''
        s2 = ''

        # Перебираем узлы связанных списков
        while list1:
            s1 = str(list1.val) + s1
            list1 = list1.next

        while list2:
            s2 = str(list2.val) + s2
            list2 = list2.next

        int1 = int(s1)
        int2 = int(s2)

        # Получаем результат сложения в виде строки и переворачиваем
        result_str = str(int1 + int2)[::-1]

        # Строим связанный список из строки
        result_list = ListNode(int(result_str[0]))
        current = result_list

        for digit in result_str[1:]:
            current.next = ListNode(int(digit))
            current = current.next

        return result_list
