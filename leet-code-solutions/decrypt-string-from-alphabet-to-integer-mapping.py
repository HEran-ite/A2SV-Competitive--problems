class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = s[i:i + 2]
                i += 3
            else:
                num = s[i]
                i += 1
            val = chr(int(num) + 96)
            lst.append(val)
        return ''.join(lst)

