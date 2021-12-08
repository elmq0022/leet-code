from DataStructures import ListNode
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = current = ListNode()

        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next

            current = current.next

        if p1:
            current.next = p1

        if p2:
            current.next = p2

        return dummy_head.next
