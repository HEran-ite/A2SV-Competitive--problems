class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums1=nums[:len(nums)/2]
        nums2=nums[len(nums)/2:]
        res=[]
        for i in range (n):
            res.append(nums1[i])
            res.append(nums2[i])
        return res
