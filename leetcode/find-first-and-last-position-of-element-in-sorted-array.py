class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums.append(inf)
        def BSr (l,r):
            while l<r:
                mid=(l+r)//2
                if nums[mid]>target:
                    r=mid
                else:
                    l=mid+1
            
            return l
        
        def BSl (l,r):
            while l<r:
                mid=(l+r)//2
                if nums[mid]>=target:
                    r=mid
                else:
                    l=mid+1
                    
            return l if l<len(nums) and nums[l]==target else -1
        left=BSl(0,len(nums)-1)
        right=BSr(0,len(nums)-1)
        if left==-1:
            return[left,left]
        return [left,right if  nums[right]==target else right-1]




        