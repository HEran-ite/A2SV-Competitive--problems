class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum=sum(nums[:k])
        max_sum=curr_sum
        for i in range(k,len(nums)):
            curr_sum+=nums[i]
            curr_sum-=nums[i-k]
            max_sum=max(curr_sum,max_sum)
        avg=max_sum/k
        return avg
