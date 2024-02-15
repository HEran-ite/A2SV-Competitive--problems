# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=-1
        dummy=ListNode(-1)
        dummy.next=head
        curr=dummy

        while curr:
            count+=1 
            last=curr
            curr=curr.next
        print(count)
        curr=head
        if count<=2:
            return dummy.next

        for i in range(count//2):
            if curr:
                print('hey')
                temp=curr.next
                curr.next=curr.next.next
                last.next=temp
                last.next.next=None
                last=last.next
                curr=curr.next
        return dummy.next



        