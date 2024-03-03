class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(opened,closed,gen):
            nonlocal res
        
            if opened==0 and closed==0:
                res.append(''.join(gen[:]))
                return 

                
            if opened < closed:
                gen.append(')')
                backtrack(opened,closed-1,gen[:])
                gen.pop()

            if opened >0:
                gen.append("(")
                backtrack(opened-1,closed,gen[:])
                gen.pop()

        backtrack(n,n,[])
        return res


 # if opened > 0:
            #     pickOpened = backtrack(opened-1,closed,gen+'(')

            # if opened < closed:
            #     pickClosed=backtrack(opened,closed-1,gen+")")