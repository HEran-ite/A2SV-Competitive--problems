class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = 0
        count = 0
        curr_sum = 0
        dic = Counter()
        dic[0] = 1
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            if curr_sum - goal in dic:
                count += dic[curr_sum - goal]
                print
            dic[curr_sum] += 1
        
        return count

