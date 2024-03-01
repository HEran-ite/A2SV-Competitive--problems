class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l,r=0,0
        count=0
        dic=Counter(nums)
        dic2=defaultdict(int)
       
        for r in range(len(nums)):
            dic2[nums[r]]+=1
            
            while l<=r and len(dic)==len(dic2):
                count+=len(nums)-r
                dic2[nums[l]]-=1
                if dic2[nums[l]]==0:
                    del dic2[nums[l]]
                l+=1

        return count