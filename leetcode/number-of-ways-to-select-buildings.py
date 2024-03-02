class Solution:
    def numberOfWays(self, s: str) -> int:
        dic=Counter(s)
        res=0
        prev0=0
        prev1=0
        for i in range (len(s)):
            if s[i]=="0":
                res+=prev1*(dic["1"]-prev1)
                prev0+=1
            else:
                res+=prev0*(dic["0"]-prev0)
                prev1+=1
        return res