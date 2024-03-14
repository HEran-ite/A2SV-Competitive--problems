# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def BS(l,r):
            while l<r:
                mid=(l+r)//2
                if isBadVersion(mid):
                    r=mid
                else:
                    l=mid+1
                
            return l if isBadVersion(l) else -1
        return BS(0,n)