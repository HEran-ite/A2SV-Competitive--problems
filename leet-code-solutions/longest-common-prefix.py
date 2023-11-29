class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        initial=strs[0]
        common=''
        for x in strs:
            if x=='':
                common==''
                return common
            elif len(x)< len(initial):
                initial=x
        

            
        for i in range (0,len(initial)):
            for j in strs:
                if initial[i]==j[i]:
                    pass
                else:
                    return common 
            common+=j[i]    
        return common    
          

