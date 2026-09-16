# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #1. removing head
        #2. removing some node in middle
        #3. removing last node
        if not head: return


        curr, curr1 = head, head
        list_size = 1
        while curr.next:
            list_size += 1
            curr = curr.next


        i = 1
        removal_node_ind = list_size - n
        while i < removal_node_ind:
            i += 1
            curr1 = curr1.next

        if removal_node_ind == 0:
            return head.next

        node_to_remove = curr1.next
        curr1.next = curr1.next.next
        node_to_remove.next = None

        return head

        