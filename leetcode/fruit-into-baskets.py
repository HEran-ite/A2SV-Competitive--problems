class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r=0,0
        max_count,count=0,0
        dic=defaultdict(int)
        for r in range(len(fruits)):
            dic[fruits[r]]+=1
            count+=1
            while len(dic)>2:
                dic[fruits[l]]-=1
                count-=1
                
                if dic[fruits[l]]==0:
                    dic.pop(fruits[l])
                l+=1

            max_count=max(max_count,count)
        return max_count
