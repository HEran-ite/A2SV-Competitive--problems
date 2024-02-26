class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtracking(idx,gen):
            nonlocal res
            res.append(gen[:])
            if idx >= len(nums):
                return
            
            for i in range (idx,len(nums)):
                gen.append(nums[i])
                backtracking(i+1,gen[:])
                gen.pop()
                
        backtracking (0,[])
        return res