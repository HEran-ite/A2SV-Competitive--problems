class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sp=gp=0
        count=0
        g.sort()
        s.sort()
        while gp<len(g) and sp<len(s):
            if g[gp]<=s[sp]:
                count+=1
                sp+=1
                gp+=1
            else:
                sp+=1
        return count

