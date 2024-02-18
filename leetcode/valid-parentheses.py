class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        map={'[':']','{':'}','(':')'}
        for par in s:
            if par in map.keys():
                stack.append(par)
            else:
                if len(stack)==0 or map[stack[-1]]!=par:
                    return False
                stack.pop()
        return len(stack)==0
            
