class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        maxGood=-1
        for i in range (len (num)-2):
            if num[i]==num[i+1]==num[i+2]:
                good=num[i]
                maxGood=max(maxGood,num[i])
        if maxGood==-1:
            return''
        return str(maxGood)+str(maxGood)+str(maxGood)