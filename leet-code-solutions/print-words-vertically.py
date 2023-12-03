class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        s=s.split()
        max_len = max(len(word) for word in s)
        for i in range(max_len):
            string=''
            for j in range (len(s)):
                if i >len(s[j])-1:
                    string+=' '                    
                else:
                    string+=s[j][i]

            res.append(string.rstrip())
        return res




