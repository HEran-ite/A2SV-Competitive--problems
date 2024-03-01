class Solution:
    def minimumSteps(self, s: str) -> int:
        count=0
        l,r=0,len(s)-1
        s=list(s)
        while l<r:
            if s[l]=="1" and s[r]=="1":
                r-=1
            
            elif s[l]=="1" and s[r]=='0':
                s[l],s[r]=s[r],s[l]
                count+=r-l
                l+=1
                r-=1
            else:
                l+=1
        return count