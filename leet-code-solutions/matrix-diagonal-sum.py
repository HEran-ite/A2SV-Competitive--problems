class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        primary=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    primary+=mat[i][j]
        i,j=0,n-1
        secondary=0
        while j>=0 and i<n:
            secondary+=mat[i][j]
            i+=1
            j-=1

        if n%2==0:
            return primary+secondary
        m=(n-1)//2
        return primary+secondary-mat[m][m]


