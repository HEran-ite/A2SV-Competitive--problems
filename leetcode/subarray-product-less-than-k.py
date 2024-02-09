class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        product = 1
        subarrays = 0
        for j in range(len(nums)):
            product *= nums[j] 
            while  product  >= k and i<=j:
                product //= nums[i] 
                i += 1 
            subarrays+=j-i+1 
        return subarrays
        