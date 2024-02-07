class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr=[0]*len(s)
        for i in range (len(shifts)):
            if shifts[i][2]==0:
                arr[shifts[i][0]]-=1
                if shifts[i][1]+1!= len(s):
                    arr[shifts[i][1]+1]+=1
            else:
                arr[shifts[i][0]]+=1
                if shifts[i][1]+1!= len(s):
                    arr[shifts[i][1]+1]-=1

        prefix_sum=0
        prefix_arr=[]
        for i in range (len(arr)):
            prefix_sum+=arr[i] 
            prefix_arr.append(prefix_sum)  
        # print(arr)   
        # print(prefix_arr)
     
        res=''
        for i in range(len(arr)):
            res+=chr(((ord(s[i])-97+prefix_arr[i]))%26 +97)
        return res