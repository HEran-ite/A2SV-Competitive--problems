class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        sum=0
        for i in range(1,len(salary)-1):
             sum+=salary[i]
        return float(sum)/(len(salary)-2)

        