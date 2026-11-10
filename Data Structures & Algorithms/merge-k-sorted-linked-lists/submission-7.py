# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        result = ListNode()
        tracker = result

        for i, head in enumerate(lists):
            if head:

                heapq.heappush(min_heap, (head.val, i, head))


        while min_heap:
            value, index, curr = heapq.heappop(min_heap)

            tracker.next = curr
            tracker = curr

            if curr.next:
                heapq.heappush(min_heap, (curr.next.val, index, curr.next))

        return result.next


        