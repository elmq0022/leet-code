from typing import Optional
from DataStructures import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # already reversed
        if not head:
            return head

        # already reversed
        if not head.next:
            return head

        # recursive call to the last node
        new_head = self.reverseList(head.next)

        # reverse
        head.next.next = head

        # break cycle
        head.next = None

        # will return second to last on first occurrence
        return new_head
