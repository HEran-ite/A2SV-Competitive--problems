class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res=[]
        dic={'2':['a','b','c'],'3':['d','e','f'],
            '4':['g','h','i'],'5':['j','k','l'],
            '6':['m','n','o'],'7':['p','q','r','s'],
            '8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits)==1:
            return dic[digits]
        def backTrack(i,curStr):
            if len(curStr)==len(digits):
                res.append(curStr)
                return 
            for c in dic[digits[i]]:
                backTrack(i+1,curStr+c)
        
        if digits:
            backTrack(0,'')
        return res