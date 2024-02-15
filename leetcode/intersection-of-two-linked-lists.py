# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a=headA
        b=headB 
        store=set()
        while a :
            store.add(a)
            a=a.next
        while b:
            if b in store:
                return b
            b=b.next
        return


