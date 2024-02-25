class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i in range (len(temperatures)):
            while stack and  stack[-1][0] < temperatures[i]:
                ind=stack[-1][1]
                res[ind]=i-ind
                stack.pop()
                
            stack.append([temperatures[i],i])
        return res
            
        
            