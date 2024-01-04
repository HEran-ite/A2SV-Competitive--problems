from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: 
        if len(p)>len(s):
            return []
        p_map=Counter(p)
        count=[]
        for i in range (len(s)-len(p)+1):
            s_map=Counter(s[i:i+len(p)])
            if s_map ==p_map:
                count.append(i)
        return count

            



