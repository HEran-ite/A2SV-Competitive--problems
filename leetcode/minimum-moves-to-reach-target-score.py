class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0   
        while target >1 :
            if maxDoubles==0:
                return count+ target-1
            elif target%2!=0: 
                target-=1
            else:
               target=int(target/2)
               maxDoubles-=1
            count+=1
        return count