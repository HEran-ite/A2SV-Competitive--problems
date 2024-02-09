class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        prefix_map=defaultdict(int)
        prefix_map[0]=1
        count=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            prefix_map[prefix_sum%k]+=1
        for num in prefix_map :
            count+=int(prefix_map[num]*(prefix_map[num]-1)/2)
        return count


   