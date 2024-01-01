import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        map={}
        res=[]
        for i in range (len(points)):
            map[(math.sqrt((points[i][0])**2+(points[i][1])**2),i)]= points[i]
        map=dict(sorted(map.items()))
        val=list(map.values())
        for i in range(k):
            res.append(val[i])
        return res

            