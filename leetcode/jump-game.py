class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        l,r=0,1
        if len(nums)<=1:
            return True
        if nums[0]==0:
            return False
        nums.reverse()
        flag=False
        
        while r<len(nums) :
            if nums[r]>=r-l:
                flag=True
                l=r
                r+=1
            else:
                r+=1
                flag=False
        return flag



        