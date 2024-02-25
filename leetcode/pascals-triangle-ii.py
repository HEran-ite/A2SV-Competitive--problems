class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(rowIndex,curr,res):
            if curr == rowIndex:
                return res
            new_res=[1]
            for i in range(curr):
                new_res.append(res[i+1]+res[i])
            new_res.append(1)
            return helper(rowIndex ,curr+1,new_res)
        return helper(rowIndex,0,[1])
            
        