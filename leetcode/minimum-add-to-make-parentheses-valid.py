class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        moves=0
        for par in s:
            if par =='(':
                stack.append(par)
            else:
                if len(stack)==0:
                    moves+=1
                else:
                    stack.pop()
        return moves+len(stack)