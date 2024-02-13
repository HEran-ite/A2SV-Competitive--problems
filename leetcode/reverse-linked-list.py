# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        arr.reverse()
        print(arr)
        if arr:
            head=ListNode(arr[0])
        curr=head
        for i in range (1,len(arr)):
            curr.next=ListNode(arr[i])
            curr=curr.next
        return head
        