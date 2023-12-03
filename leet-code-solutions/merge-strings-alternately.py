class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l=min(len(word1),len(word2))
        res=[]
        for i in range (l):
            res.append(word1[i])
            res.append(word2[i])
        res.append(word1[l:len(word1)])
        res.append(word2[l:len(word2)])
        res=''.join(res)
        return res
            