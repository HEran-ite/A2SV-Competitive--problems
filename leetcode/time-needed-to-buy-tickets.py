from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=deque([])
        count=0
        for i in range(len(tickets)):
            queue.append([tickets[i],i])
        print(queue) 
        while queue :
            queue[0][0]-=1
            if queue[0][0]>0:
                queue.append(queue[0])
            if queue[0][1]==k and queue[0][0]==0 :
                return count+1
            queue.popleft()
            count+=1
        return count


