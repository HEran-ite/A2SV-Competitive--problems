class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxWidth=0
        points.sort()
        for i in range(len(points)-1):
            dif=points[i+1][0]-points[i][0]
            maxWidth=max(maxWidth,dif)
        return maxWidth
