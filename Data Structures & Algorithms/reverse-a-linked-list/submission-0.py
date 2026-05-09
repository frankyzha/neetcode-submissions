# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # (1,2) (2,3) (3,4)
        # (4,3) ()
        nodes: list[ListNode] = [None]

        node = head
        while node is not None:
            nodes.append(node)
            node = node.next
        
        for i in range(len(nodes)-1, 0, -1):
            nodes[i].next = nodes[i-1]
        
        return nodes[-1]