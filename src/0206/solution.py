from typing import Optional
from DataStructures import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = current = post = head
        post = post.next
        head.next = None

        while post:
            current = post
            post = post.next
            current.next = prev
            prev = current

        return current
