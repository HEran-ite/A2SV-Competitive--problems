class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words)-1):
            l=min(len(words[i]),len(words[i+1]))
            for j in range(l):
                
                if words[i][j]!=words[i+1][j] :
                    if order.index(words[i][j])>order.index(words[i+1][j]):
                        return False
                    break
            else:
                if len(words[i]) >len(words[i+1]):
                    return False

        return True
            
                
            


        