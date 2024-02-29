class Solution:
    def maxSumRangeQuery(self, nums: List[int], req: List[List[int]]) -> int:
        freq=[0]*len(nums)    
        for i in range(len(req)):
            freq[req[i][0]]+=1
            if(req[i][1]<len(nums)-1):
                freq[req[i][1]+1]-=1
        
        for i in range(len(nums)):
            if(i==0):
                continue
            freq[i]+=freq[i-1]

        freq.sort()
        nums.sort()
        ans=0
        N=1000000000 + 7
        for i in range(len(nums)-1,-1,-1):
            ans+=(freq[i]*nums[i])%N
            ans%=N
        return int(ans%N)