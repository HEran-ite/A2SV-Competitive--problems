class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positive=[]
        negative=[]
        merged=[]
        for i in range (len(nums)):
            if abs(nums[i])==nums[i]:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range (len(nums)/2):
            merged.append(positive[i])
            merged.append(negative[i])
        return merged

