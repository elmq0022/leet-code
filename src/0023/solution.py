import heapq
from typing import List

from src.DataStructures import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        head = ListNode()
        current = head

        for node in lists:
            if node:
                # patch ListNode with < operator for heapq to work properly
                node.__class__.__lt__ = lambda self, other: self.val < other.val
                heapq.heappush(heap, node)

        while heap:
            node = heapq.heappop(heap)
            if node.next:
                # patch ListNode with < operator for heapq to work properly
                node.__class__.__lt__ = lambda self, other: self.val < other.val
                heapq.heappush(heap, node.next)
            current.next = node
            current = current.next

        return head.next
