class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum=[]
        sums=0
        for i in range(len(nums)):
           sums+=nums[i] 
           running_sum.append(sums)
        return running_sum
