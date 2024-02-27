class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(idx,gen):
            nonlocal res
            if idx== len(nums):
                res.append(gen[:])
                return
            
            for i in range (len(nums)):
                if gen and nums[i] in gen[:]:
                    pass
                else:
                    gen.append(nums[i])
                    backtrack(idx+1,gen[:])
                    gen.pop()
        backtrack(0,[])
        return res