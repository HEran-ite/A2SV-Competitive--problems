from collections import Counter
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=r=0
        dic=Counter()
        max_sum=0
        sums=0
        
        while r<len(nums):
            if dic[nums[r]]==0:
                dic[nums[r]]+=1
                sums+=nums[r]
                max_sum=max(max_sum,sums)
                r+=1
            else:
                sums-=nums[l]
                dic[nums[l]]-=1
                l+=1
        return max_sum


