class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count=0
        maxNum=nums[0]
        for i in range(1, len(nums)):
            if nums[i] < maxNum:
                maxNum = nums[i]
                count += i
        return count


        
        