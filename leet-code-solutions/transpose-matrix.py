class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in range(len(matrix[0])):
            container=[]
            for j in range(len(matrix)):
                container.append(matrix[j][i])
            res.append(container)
        return res
                