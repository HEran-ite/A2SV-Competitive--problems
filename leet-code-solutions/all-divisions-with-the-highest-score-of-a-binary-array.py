class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # lst=[]
        # for i in range(len(nums)):
        #     left=len(nums)-len(nums[i+1:])-sum(nums[:i])
        #     right=sum(nums[i+1:])
        #     lst.append(left+right)
        # maxSum=max(lst)
        # res=[]
        # for i in range(len(lst)):
        #     if lst[i]==maxSum:
        #         res.append(i)
        # return res 
        one = one_2 = Counter(nums)[1]
        zeros = zeros_2 = 0
        high = 0

        for i, j in enumerate(nums):
            high = max(high, one + zeros)
            if j == 1:
                one -=1
            else:
                zeros += 1
        high = max(high, one + zeros)
        output=[]


        for i, j in enumerate(nums):
            if high == one_2 + zeros_2:
                output.append(i)
            if j == 1:
                one_2 -= 1
            else:
                zeros_2 += 1

        if high == one_2 + zeros_2:
            output.append(len(nums))

        return output