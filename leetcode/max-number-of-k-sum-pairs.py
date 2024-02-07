class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l,r=0,len(nums)-1
        count=0
        nums.sort()
        while l<r :
            cur_sum=nums[l]+nums[r]
            if cur_sum>k:
                r-=1
            elif cur_sum <k:
                l+=1
            else:
                count+=1
                l+=1
                r-=1
        return count

