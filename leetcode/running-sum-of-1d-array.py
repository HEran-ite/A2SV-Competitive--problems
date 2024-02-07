class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur_sum=0
        res=[]
        for i in range(len(nums)):
            cur_sum+=nums[i]
            res.append(cur_sum)
        return res
