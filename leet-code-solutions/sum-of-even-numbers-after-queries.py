class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        evenSum=0
        lst=[]
        for i in range (len(nums)):
            if nums[i]%2==0:
                evenSum+=nums[i]

        for i in range (len(queries)):
            if nums[queries[i][1]]%2==0:
                evenSum-=nums[queries[i][1]]
            nums[queries[i][1]]+=queries[i][0]
            if nums[queries[i][1]]%2==0:
                evenSum+=nums[queries[i][1]]
            lst.append(evenSum)
        return lst
            

