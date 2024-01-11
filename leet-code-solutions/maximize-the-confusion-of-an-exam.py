class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l,r=0,0
        dic ={"T":0,"F":0}
        maxLen=0
        for r in range(len(answerKey)):
            dic[answerKey[r]]+=1
            while min(dic["T"],dic["F"])>k:
                dic[answerKey[l]]-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen