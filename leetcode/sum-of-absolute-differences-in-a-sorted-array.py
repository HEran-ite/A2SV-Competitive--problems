class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res=[]
        prefix_arr=[]
        prefix_sum=0
        for i in range (len(nums)):
            prefix_sum+=nums[i]
            prefix_arr.append(prefix_sum)
        print(prefix_arr)
        for i in range(len(nums)):
            if i==0:
                diff=((prefix_arr[-1]-prefix_arr[i]) - (nums[i]*(len(nums)-i-1)))
            else:
                diff=(nums[i]*i)-prefix_arr[i-1] + ((prefix_arr[-1]-prefix_arr[i]) - (nums[i]*(len(nums)-i-1)))
            res.append(diff)
        return res