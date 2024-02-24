class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic=defaultdict(int)
        max_len=0
        l,r=0,0
        max_count,count=float(-inf),0
        for r in range(len(s)):
            dic[s[r]]+=1
            while r-l+1-max(dic.values()) > k :
                dic[s[l]]-=1
                l+=1
            count=r-l+1

            max_count=max(count,max_count)

        return max_count