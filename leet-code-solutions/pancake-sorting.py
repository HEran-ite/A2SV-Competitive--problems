class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            maxInd = arr.index(max(arr[:len(arr)-i]))
            arr[:maxInd+1] = reversed(arr[:maxInd+1])
            res.append(maxInd + 1)
            
            arr[:len(arr)-i] = reversed(arr[:len(arr)-i])
            res.append(len(arr)-i)
           
        return res

            