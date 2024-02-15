# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lst=head
        dummy1=ListNode(-1)
        curr1=dummy1
        dummy2=ListNode(-1)
        curr2=dummy2

        while lst :
            temp=lst.next
            lst.next=None
            if lst.val<x:
                curr1.next=lst
                curr1=curr1.next
            elif lst.val>=x:
                curr2.next=lst
                curr2=curr2.next
            lst=temp
        curr1.next=dummy2.next
        return dummy1.next