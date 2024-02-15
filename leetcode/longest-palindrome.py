class Solution:
    def longestPalindrome(self, s: str) -> int:
        map=Counter(s)
        values=map.values()
        ans=0
        flag=False
        for num in values:
            if num%2==0:
                ans+=num
            else:
                ans+=num-1
                flag=True
        if flag:
            return ans+1
        return ans