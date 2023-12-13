class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        above=[]
        below=[]
        equal=[]
        for i in range (len(nums)):
            if nums[i] > pivot:
               above.append(nums[i])
            elif nums[i] < pivot:
               below.append(nums[i])
            else:
                equal.append(nums[i])
        return below+equal+above
