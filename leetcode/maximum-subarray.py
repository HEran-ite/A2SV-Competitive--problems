class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum=0
        mx_sum=float(-inf)
        for i in range(len(nums)):
            if prefix_sum<0:
                prefix_sum=0
            prefix_sum+=nums[i]
            mx_sum=max(mx_sum,prefix_sum)
        return mx_sum