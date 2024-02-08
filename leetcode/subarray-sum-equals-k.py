class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        prefix_map=defaultdict(int)
        prefix_map[0]=1 # for sum you should 
        count=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            count+=prefix_map[prefix_sum-k]
            prefix_map[prefix_sum]+=1
            
        return count































