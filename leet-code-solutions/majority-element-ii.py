class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        majorityNum=[]
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in freq:
            if freq[num] > len(nums)/3:
                majorityNum.append(num)
        return majorityNum



