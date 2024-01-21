class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            if i==0 and sum(nums[1:len(nums)])==0:
                return 0
            elif i==len(nums)-1 and sum(nums[:len(nums)-1])==0:
                return i
            elif sum(nums[:i])== sum(nums[i+1:]):
                return i
        return -1    