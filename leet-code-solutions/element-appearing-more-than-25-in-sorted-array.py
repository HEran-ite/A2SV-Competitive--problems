class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq={}
        for i in range (len(arr)):
            if arr[i] in freq:
                freq[arr[i]]+=1
            else:
                freq[arr[i]]=1
        for i in range (len(arr)):
            if float(freq[arr[i]])/len(arr) >0.25:
                return arr[i]