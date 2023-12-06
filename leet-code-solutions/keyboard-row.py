class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        default=row1
        for word in words:
            lword= word.lower()
            if lword[0] in row1:
                default=row1
            elif lword[0] in row2:
                default=row2
            elif lword[0] in row3:
                default=row3
            for i in range (len(word)):
                if lword[i] not in default:
                   break
            else:
                res.append(word)
        return res       
                          




