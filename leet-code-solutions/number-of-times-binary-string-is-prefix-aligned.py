class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cur_max=0
        count=0
        for i in range (len(flips)):
            cur_max=max(cur_max,flips[i])
            if cur_max== i+1:
                count+=1
        return count