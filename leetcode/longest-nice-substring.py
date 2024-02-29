class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s :
            return ""
        set_s=set(s)
        for i,ltr in  enumerate(s):        
            if ltr.swapcase() not in set_s:
                
                s_left = self.longestNiceSubstring(s[:i])
                s_right = self.longestNiceSubstring(s[i+1:])

                if len(s_left)>=len(s_right):
                    return s_left
                return s_right

        return s
