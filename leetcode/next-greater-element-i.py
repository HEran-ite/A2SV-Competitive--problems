class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res=[-1]*(len(nums1))
       
        for i in range(len(nums2)):
            if not stack:
                stack.append(nums2[i])
                
            while stack and nums2[i]>stack[-1]:
                if stack[-1] in nums1:
                    res[nums1.index(stack[-1])]=nums2[i]
                stack.pop()
            stack.append(nums2[i])

        return res       
            