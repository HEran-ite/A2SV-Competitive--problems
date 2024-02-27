class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(opened,closed,gen):
            nonlocal res
            if opened==0 and closed==0:
                res.append(gen[:])
                return 

            if opened > 0:
                pickOpened = backtrack(opened-1,closed,gen+'(')

            if opened < closed:
                pickClosed=backtrack(opened,closed-1,gen+")")
                

        backtrack(n,n,"")
        return res
