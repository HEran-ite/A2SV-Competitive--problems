class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        pHolder,seeker=0,1
        count=0
        while pHolder<seeker and seeker<len(nums):
            if nums[pHolder]+nums[seeker]<target:
                count+=1
                seeker+=1
            else :
                pHolder+=1
                seeker=pHolder+1
            if  seeker==len(nums):
                pHolder+=1
                seeker=pHolder+1
        return count