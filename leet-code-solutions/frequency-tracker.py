class FrequencyTracker:

    def __init__(self):
        self.freq=collections.defaultdict(int)
        self.val=collections.defaultdict(int)
        

    def add(self, number: int) -> None:
        self.freq[number]+=1
        n=self.freq[number]
        self.val[n]+=1
        self.val[n-1]-=1


        

    def deleteOne(self, number: int) -> None:
        if self.freq[number]>0:
            self.freq[number]-=1
            n=self.freq[number]
            self.val[n]+=1
            self.val[n+1]-=1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.val[frequency] >0




        # for i in freq.values():
        #     if frequency==i:
        #         return True
        # else:
        #     return False


        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)