class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[1])
        print(points)
        l,r=0,1
        count=1
        while l<r and r<len(points):
            if points[l][1]<points[r][0]:
                count+=1
                l=r
            r+=1
        return count
                
