class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic=Counter(answers)
        total=0
        for num,freq in dic.items():
            total+= (num+1)*(math.ceil(freq/(num+1)))          
        return int(total)


