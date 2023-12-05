class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxPer=0
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2]:
                perimeter=nums[i]+nums[i+1]+nums[i+2]
                maxPer=max(maxPer,perimeter)
        return maxPer
