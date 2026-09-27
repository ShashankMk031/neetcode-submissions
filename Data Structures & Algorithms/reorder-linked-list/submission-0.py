# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head 
        while fast and fast.next: 
            fast = fast.next.next 
            slow = slow.next 
        # slow at center so to add values 
        # Now reversal 
        second = slow.next # split 
        slow.next = None 
        # reversal 
        curr = second 
        prev = None 
        while curr: 
            nxt = curr.next 
            curr.next = prev  
            prev = curr  
            curr = nxt
        second = prev 
        # merge 
        first = head 
        while second: 
            first_nxt = first.next 
            sec_nxt = second.next 
            first.next = second 
            second.next = first_nxt 
            
            first = first_nxt 
            second = sec_nxt 
        #return head 