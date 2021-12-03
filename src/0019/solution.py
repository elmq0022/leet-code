from typing import Optional

from src.DataStructures import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = head

        for _ in range(n):
            p2 = p2.next

        if not p2:
            return p1.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        return head
