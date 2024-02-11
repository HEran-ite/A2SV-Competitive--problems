class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r=0,len(cardPoints)-k
        cur_sum=sum(cardPoints[r:])

        max_sum=cur_sum
        
        while l<r and r<len(cardPoints):
            cur_sum-=cardPoints[r]
            cur_sum+=cardPoints[l]
            max_sum=max(max_sum,cur_sum)
            l+=1
            r+=1    
        return max_sum
            