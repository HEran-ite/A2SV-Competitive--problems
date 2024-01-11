class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r=0,0
        dic ={0:0,1:0}
        maxLen=0
        for r in range(len(nums)):
            dic[nums[r]]+=1
            while dic[0]>k:
                dic[nums[l]]-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen