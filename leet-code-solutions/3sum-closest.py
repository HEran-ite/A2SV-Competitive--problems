class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        cur_sum = float('inf')  
        
        for i in range(len(nums) - 2):
            l,r= i + 1, len(nums) - 1 
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < abs(target - cur_sum):
                    cur_sum = total
                
                if total < target:
                    l+=1
                elif total > target:
                    r-=1
                else: 
                    return cur_sum
        
        return cur_sum
