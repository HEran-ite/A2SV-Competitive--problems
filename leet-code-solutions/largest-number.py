class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]

        str_nums.sort(reverse=True)
        
        swap = False 
        while not swap:
            swap = True
            for i in range(len(str_nums)-1):
                if str_nums[i]+str_nums[i+1] < str_nums[i+1]+str_nums[i]:
                    str_nums[i], str_nums[i+1] = str_nums[i+1], str_nums[i]
                    swap = False        
        res = "".join(str_nums)

        if res[0] == '0':
            return str(0)
        
        return res


                

       