class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        res=[]
        candidates=[1,2,3,4,5,6,7,8,9]
        def backtrack(gen,idx,summ): 
            nonlocal res
            if summ ==target and len(gen)==k :
                res.append(gen[:])
                return  

            elif summ >target or idx >=len(candidates):
                return  

            gen.append(candidates[idx])
            backtrack(gen,idx+1, summ + candidates[idx])
            gen.pop()


            curr=candidates[idx]
            while idx<len(candidates) and curr==candidates[idx]:
                    idx+=1
            backtrack(gen,idx,summ)

        backtrack([],0,0)
        return res