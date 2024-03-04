# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l=0
        curr=head

        while curr:
            curr=curr.next
            l+=1
        
        spaces=l//k
        additional=l%k

        curr=head
        res=[]
        for i in range (k):
            res.append(curr)

            for j in range (spaces-1+(1 if additional >0 else 0)):
                print(additional)
                if not curr:
                    break
                curr=curr.next
            additional-=1
            
            if curr:
                curr.next,curr=None,curr.next
          
                
        return res 
