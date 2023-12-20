class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len (digits)):
            digits[i]=str(digits[i])

        digits=''.join(digits) 
        num=str(int(digits)+1)
        res=list(num)

        for i in range(len (res)):
            res[i]=int(res[i])
            
        return res