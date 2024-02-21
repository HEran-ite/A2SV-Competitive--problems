class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a=sorted(costs,key=lambda x:x[0]+-x[1])
        res=0
        n=len(costs)
        for i in range(n):
            if i < n //2:
                res+=a[i][0]
            else:
                res+=a[i][1]
        return res
        