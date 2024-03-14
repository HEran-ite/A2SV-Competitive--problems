class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validator(capacity):
            count=1
            summ=0
            for r in range(len(weights)):
                
                while summ +weights[r] > capacity and r<len(weights):
                    summ=0
                    count+=1
                summ+=weights[r]
            return True  if count <=days else False

        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if validator(mid):
                high=mid
            else:
                low=mid+1
        return low
                
