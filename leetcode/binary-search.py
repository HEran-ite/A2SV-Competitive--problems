class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def BS(l,r):
            
            while l<r:
                mid=(l+r)//2

                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid
                return BS(l,r)
            return l if nums[l]==target else -1
        return BS(0,len(nums)-1)
        
            
        

