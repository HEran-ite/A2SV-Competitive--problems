class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={}
        for i in range (len(nums)):
            dic[nums[i]]=i

        for j in range (len(operations)):
            index=dic[operations[j][0]]
            
            nums[index]=operations[j][1]
            dic[nums[index]]= index
        return nums