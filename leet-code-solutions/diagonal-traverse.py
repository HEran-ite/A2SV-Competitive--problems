class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic=defaultdict(list)
        res=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i+j].append(mat[i][j])
        for idxSum in dic:
            if idxSum%2==0:
                dic[idxSum].reverse()
                print(dic[idxSum])
            for k in range(len(dic[idxSum])):
                res.append(dic[idxSum][k])
                
        return res
            
