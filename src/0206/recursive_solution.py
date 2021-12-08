from typing import Optional
from DataStructures import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # already reversed return
        if not head or not head.next:
            return head

        # recursive call to the last node
        new_head = self.reverseList(head.next)

        # reverse
        head.next.next = head
        head.next = None

        # will last node on first occurrence and there after
        return new_head
