# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #intuition: have a curr that collects the next smallest node from either list, choose the smaller head value to be the next curr, curr stores the new list, then return the start of curr
        curr = start = ListNode()
        while list1 and list2:

            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        #if remaining amount in one of the list
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return start.next