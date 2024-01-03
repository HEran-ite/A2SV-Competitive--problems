class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker=1
        pholder=0
        while seeker<len(nums):
            if nums[seeker]!=0 and nums[pholder]==0:
                nums[pholder],nums[seeker]=nums[seeker],nums[pholder]
                pholder+=1
            elif nums[pholder]!=0:
                pholder+=1
            seeker+=1     
        return nums
                

