class Solution:
    def minimizedStringLength(self, s: str) -> int:
        dic={}
        count=0
        for i in range(len(s)) :
            if s[i] in dic:
               pass
            else:
                dic[s[i]]=1
                count+=1
        return len(dic)
           