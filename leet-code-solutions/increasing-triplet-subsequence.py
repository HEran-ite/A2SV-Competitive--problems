class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smaller=float(inf)
        smallest=float(inf)
        for i in range(len(nums)):
            if nums[i]<=smallest:
                smallest=nums[i]
            elif nums[i] <= smaller:
                smaller=nums[i]
            else:
                return True
                 
        return False

                

        

