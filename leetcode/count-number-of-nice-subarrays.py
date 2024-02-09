class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.counter(nums,k)-self.counter(nums,k-1)
    def counter(self,nums,k):
            l,r=0,0
            dic={'even':0,"odd":0}
            count=0
            for r in range (len(nums)):
                if nums[r]%2!=0:
                    dic["odd"]+=1
                while dic["odd"]>k:
                    
                    if nums[l]%2!=0:
                        dic["odd"]-=1
                    l+=1
                count+=r-l+1
                r+=1 
            return count 
        
    