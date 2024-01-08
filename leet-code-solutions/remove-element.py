class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_nums = []
        for num in nums:
            if num != val:
                new_nums.append(num)
        nums[:] = new_nums  
        return len(new_nums)