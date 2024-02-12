# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.dummy=Node()
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k=0
        curr=head
        while curr:
            curr=curr.next
            k+=1  
        curr=head
        prev=None
        for i in range (k-n):
            prev=curr
            curr=curr.next
        if not prev:
            return head.next
            
        prev.next=curr.next    
        return head
