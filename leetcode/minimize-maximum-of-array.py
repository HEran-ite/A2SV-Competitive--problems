class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        mx=max(nums)
        summ=0
        max_avg=float(-inf)
        for i in range (len(nums)):
            summ+=nums[i]
            avg=math.ceil(summ/(i+1))
            max_avg=max(avg,max_avg)
        return max_avg     