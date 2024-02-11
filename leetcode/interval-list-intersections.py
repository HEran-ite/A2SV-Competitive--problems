
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j, res = 0,0, []
        while(i < len(firstList) and j < len(secondList)):
            arr1 = firstList[i]
            arr2 = secondList[j]
            if arr1[0] <= arr2[0] <= arr1[1] or arr2[0] <= arr1[0] <= arr2[1]:
                interval = [max(arr1[0], arr2[0]), min(arr1[1], arr2[1])]
                res.append(interval)
        
            if arr1[1] <= arr2[1]:
                i += 1 
            if arr2[1] <= arr1[1]:
                j += 1 
        return res



