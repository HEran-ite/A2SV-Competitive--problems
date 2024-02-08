class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_ps=[1]
        backward_ps=[1]
        cur_product=1
        prefix_sum=[0]*len(nums)
        for i in range (len(nums)-1):
            cur_product*=nums[i]
            forward_ps.append(cur_product)
       
       
        nums.reverse()
        cur_product=1
        for i in range (len(nums)-1):
            cur_product*=nums[i]
            backward_ps.append(cur_product)
        backward_ps.reverse()


        for i in range (len(nums)):
            prefix_sum[i]+=backward_ps[i]*forward_ps[i]
        return prefix_sum










        # res=[]
        # for i in range (len(nums)):
        #     restore=nums[i]
        #     nums[i]=1
        #     product=1
        #     for j in range (len(nums)):
        #         product*=nums[j]
        #     nums[i]=restore
        #     res.append(product)
        # return res