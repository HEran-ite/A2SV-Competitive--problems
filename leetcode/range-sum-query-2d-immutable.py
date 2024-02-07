class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.prefix_arr= [[0 for _ in range(len(self.matrix[0])+1 )] for _ in range(len(self.matrix)+1 )]
        
        for i in range (len (self.matrix)):
            for j in range (len(self.matrix [0])):
                self.prefix_arr[i][j] = self.prefix_arr[i-1][j] + self.prefix_arr[i][j-1] - self.prefix_arr[i-1][j-1] +  self.matrix[i][j]
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:

        submatrix_sum = self.prefix_arr[r2][c2] - self.prefix_arr[r2][c1 - 1] - self.prefix_arr[r1 - 1][c2 ] + self.prefix_arr[r1 - 1][c1 - 1]
        return submatrix_sum



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)