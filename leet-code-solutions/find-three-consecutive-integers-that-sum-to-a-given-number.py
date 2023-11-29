class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        x=float((num-3))/3
        if int(x)==x:
            x=int(x)
            return[x,x+1,x+2]
        else:
            return []