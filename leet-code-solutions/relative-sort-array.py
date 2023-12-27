class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        lst=[]
        lst2=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j]== arr2[i]:
                    lst.append(arr1[j])
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                lst2.append(arr1[i])
        for i in range(len(lst2)):
            for j in range(len(lst2)-1):
                if lst2[j]>lst2[1+j]:
                    lst2[j],lst2[1+j]=lst2[j+1],lst2[j]
        return lst+lst2
        