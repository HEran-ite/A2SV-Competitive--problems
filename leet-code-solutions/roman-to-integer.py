class Solution(object):
    def romanToInt(self,s):
        dic={
            'I':'1',
            'V':'5',
            'X':'10',
            'L':'50',
            'C':'100',
            'D':'500',
            'M':'1000'

        }
        res=0
        lst=[]
        
        print(s)
        for i in range (len(s)):
           if s[i] in s:
               lst.append(int(dic[s[i]]))

        for j in range (len(lst)-1):
            if lst[j]>=lst[j+1]:
                res+=lst[j]
            else:
                res-=lst[j]
        res+=lst[len(lst)-1]
        return res



        
