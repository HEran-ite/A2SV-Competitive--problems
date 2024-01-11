class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        min_len=len(nums)+1
        sums=0
        for r in range (len(nums)):
            sums+=nums[r]
            while sums >= target:
                min_len=min(min_len,r-l+1)
                sums-=nums[l]
                l+=1
        if min_len!= len(nums)+1:
            return min_len 
        else:
            return 0
            