class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def backtracking(idx,gen):
            if len(gen) == k :
                res.append(gen[:])
                return 

            for i in range(idx+1,n-(k-len(gen))+2):
                gen.append(i)
                backtracking(i,gen)
                gen.pop()

        backtracking(0,[])
        return res


                