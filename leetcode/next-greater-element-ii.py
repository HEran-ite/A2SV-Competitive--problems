class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        stack=[]
        max_num=float(-inf)
        for i in range (len(nums)) :
            max_num =max(max_num,nums[i])
            while stack and  stack[-1][0] < nums[i]:
               res[stack[-1][1]]= nums[i] 
               stack.pop()
            stack.append([nums[i],i])
            
        for i in range (len(nums)) :    
            while stack and  stack[-1][0] < nums[i]:
                res[stack[-1][1]]= nums[i] 
                stack.pop()    
                
        return res