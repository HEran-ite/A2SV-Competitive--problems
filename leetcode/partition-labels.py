class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def merge(intervals):
            intervals=sorted(intervals,key=lambda x:x[0] )
            res=[intervals[0]]
            for i in range (len(intervals)):
                if res[-1][0]<= intervals[i][0]<=res[-1][1]:
                    res[-1][1]=max(intervals[i][1],res[-1][1])
                else:
                    res.append(intervals[i])
            return res

        rev_s=s[::-1]
        set_s=set()
        arr=[]
        for letter in s:
            if letter not in set_s:
                arr.append([s.index(letter),len(s)-rev_s.index(letter)-1])
                set_s.add(letter)
        print(arr)
        arr=merge(arr)
        print(arr)
        ans=[]
        for i in range(len(arr)):
            length=arr[i][1]-arr[i][0]+1
            ans.append(length)
        return ans
    

        
        
        

        