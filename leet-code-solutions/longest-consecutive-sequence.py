class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums = list(set(nums))  # Remove duplicates

        nums.sort()
        count = 1
        max_count = 1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] - 1:
                count += 1
            elif nums[i] != nums[i + 1]:
                count = 1
            max_count = max(max_count, count)

        return max_count