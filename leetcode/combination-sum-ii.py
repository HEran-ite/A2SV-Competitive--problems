class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(gen,idx,summ): 
            nonlocal res
            

            if summ ==target :
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