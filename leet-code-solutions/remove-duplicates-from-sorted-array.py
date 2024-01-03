from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map=Counter(nums)
        k=len(map)
        pHolder,seeker=0,1
        while pHolder<len(nums) and seeker<len(nums):
            if nums[pHolder]==nums[seeker]:
                nums[seeker]=float(inf)
                seeker+=1
            else:
                pHolder=seeker
                seeker+=1
        nums.sort()
        return k
