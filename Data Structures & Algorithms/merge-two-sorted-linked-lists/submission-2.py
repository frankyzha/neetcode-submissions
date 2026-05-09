# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            head = list1
            p1 = list1.next
            p2 = list2
        else:
            head = list2
            p1 = list1
            p2 = list2.next

        node = head
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                node.next = p1
                p1 = p1.next
                node = node.next
            else:
                node.next = p2
                p2 = p2.next
                node = node.next

        if p1 is not None:
            node.next = p1
        elif p2 is not None:
            node.next = p2

        return head