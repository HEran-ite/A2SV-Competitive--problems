from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = Counter(nums1)
        map2 = Counter(nums2)
        common = map1 & map2
        res = []

        for num in common:  
            freq = min(map1[num], map2[num])
            for i in range(freq): 
                res.append(num)
        return res
        
        