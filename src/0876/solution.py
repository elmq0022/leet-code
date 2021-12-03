from typing import Optional

from src.DataStructures import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = p2 = head

        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        if p2.next:
            p1 = p1.next

        return p1
