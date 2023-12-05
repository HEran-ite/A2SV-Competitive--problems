class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst=[]
        if len(nums)==1:
            if nums[0]==0:
                return 0
            else:
                return 1
        for i in range(len(nums)):
            if nums[i]==0:
                lst.append(i)
        if not lst:
            return len(nums)
        dif=lst[0]
        for i in range (len(lst)-1):
            dif=max(dif,lst[i+1]-lst[i]-1)
        dif=max(dif,len(nums)-1-lst[len(lst)-1])
        return dif