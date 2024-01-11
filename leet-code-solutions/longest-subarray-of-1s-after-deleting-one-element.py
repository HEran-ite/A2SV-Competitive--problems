from collections import Counter
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # zeros_ind = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         zeros_ind.append(i)
        # if len(zeros_ind)==len(nums):
        #     return 0
        # if len(zeros_ind) <= 1:
        #     return len(nums) - 1

        # max_dif = max(zeros_ind[0],len(nums) - zeros_ind[-1] - 1)

        # l, r = 0, 2

        # while r < len(zeros_ind):
        #     dif = zeros_ind[r] - zeros_ind[l] - 1
        #     max_dif = max(max_dif, dif)
        #     l += 1
        #     r += 1

        # return max_dif
        l,r=0,0
        dic ={0:0,1:0}
        maxLen=0
        for r in range(len(nums)):
            dic[nums[r]]+=1
            while dic[0]>1:
                dic[nums[l]]-=1
                l+=1
            maxLen=max(maxLen,r-l)
        return maxLen
            




