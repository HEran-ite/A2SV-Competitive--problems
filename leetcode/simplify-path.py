class Solution:
    def simplifyPath(self, path: str) -> str:
        s= path.split('/')
        stack=[]
        for item in s:
            if  item =='..':
                if len(stack)==0 :
                    pass
                else:
                    stack.pop()
            elif item=='.' or item=='':
                pass
            else:
                stack.append(item)
        return '/'+'/'.join(stack)