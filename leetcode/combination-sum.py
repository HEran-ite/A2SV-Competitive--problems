class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]

        candidates.sort()
        def backtrack(gen,idx,summ): 
            nonlocal res
            if summ >target:
                return

            elif summ ==target :
                res.append(gen[:])
                # print(res)
                return

            for i in range (idx ,len(candidates)):

                if target-candidates[i]<0 :
                    return

                else:
                    gen.append(candidates[i])
                    backtrack(gen,i, summ + candidates[i])
                    gen.pop()

        backtrack([],0,0)
        return res

