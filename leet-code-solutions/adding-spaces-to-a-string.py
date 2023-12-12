class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        if not spaces:
            return s
        lst = []
        for i in range(len(spaces)):
            if i ==0 and i == len(spaces) - 1:
                lst.append(s[0:spaces[i]])
                lst.append(s[spaces[i]:])
            elif i == 0:
                lst.append(s[0:spaces[i]])
                
            elif i == len(spaces) - 1:
                lst.append(s[spaces[i - 1]:spaces[i]])
                lst.append(s[spaces[i]:])
            else:
                lst.append(s[spaces[i - 1]:spaces[i]])
        
        return ' '.join(lst)