class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtracking(idx,gen):
            nonlocal res
            if gen[:] not in res:
                res.append((gen[:]))
            if idx >= len(nums):
                return
            
            for i in range (idx,len(nums)):
                gen.append(nums[i])
                backtracking(i+1,sorted(gen[:]))
                gen.pop()
                
        backtracking (0,[])
        
        return res