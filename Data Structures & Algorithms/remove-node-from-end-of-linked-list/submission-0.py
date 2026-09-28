# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [] 
        cur = head 
        while cur: 
            nodes.append(cur)
            cur = cur.next 
        rem_id = len(nodes) - n 
        if rem_id == 0: 
            return head.next 
        nodes[rem_id-1].next = nodes[rem_id].next 
        return head 