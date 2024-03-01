import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max=[0]*len(grid)
        col_max=[0]*len(grid[0])
        grid=np.array(grid)
        total=0
        for i in range(len(grid)):
            row_max[i]=max(grid[i])
        
        trans_grid=np.transpose(grid)
        for i in range(len(trans_grid)):
            col_max[i]=max(trans_grid[i])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total+=min(row_max[i],col_max[j])-grid[i][j]
        return total
