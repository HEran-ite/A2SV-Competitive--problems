class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for fast in range(len(nums)):
            seen=set()
            while True:
                if fast in seen:            
                    return True
                seen.add(fast)
                slow=fast
                fast=(fast+nums[fast])%len(nums)        
                if slow==fast:      
                    break
                if nums[fast]>0 and nums[slow]<0 or nums[fast]<0 and nums[slow]>0 : 
                    break           
        return False      

           
                

      