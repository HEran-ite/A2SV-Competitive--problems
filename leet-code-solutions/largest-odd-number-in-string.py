class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        num=num[::-1]
        for i in range (len(num)):
            if int(num[i])%2!=0:
                res=num[i:]
                return res[::-1]
        return ''
