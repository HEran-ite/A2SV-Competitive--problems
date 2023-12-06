class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res=[]
        maxCandies=candies[0]
        for candy in candies:
            maxCandies=max(maxCandies,candy)

        for i in range(len(candies)):
            kid=candies[i]+extraCandies
            if kid>=maxCandies:
                res.append(True)
            else:
                res.append(False)       
        return res
