

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        summ = sum(nums)
        target_mod = summ % p
        prefix_sum = 0
        min_len = float('inf')
        prefix_map = {0: -1}
        
        if target_mod == 0:
            return 0
        
        
        
        for i, num in enumerate(nums):
            prefix_sum += num
            curr_mod = prefix_sum % p
            

            needed_mod = (curr_mod - target_mod) % p
            
            if needed_mod in prefix_map:
                min_len = min(min_len, i - prefix_map[needed_mod])
            

            prefix_map[curr_mod] = i
        
        if min_len == float('inf') or min_len == len(nums):
            return -1
        
        return min_len
