class Solution:
    def sortSentence(self, s: str) -> str:
        lst=s.split() 
        dic={} 
        for i in range (len(lst)):
           dic[lst[i][-1]]= lst[i][:-1]
        sorted_dict = dict(sorted(dic.items()))
        return ' '.join(sorted_dict.values())

        