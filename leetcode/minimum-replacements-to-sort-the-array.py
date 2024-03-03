class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        splits=0
        r=nums[-1]

        for i in range(len(nums)-2,-1,-1):
            l=nums[i]
            if l>r:
                spaces=math.ceil(l/r)
                splits+=spaces-1
                r=l//spaces
            else:
                r=l
        return splits