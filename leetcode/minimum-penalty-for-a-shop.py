class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count={"Y":customers.count('Y'),"N":0}
        arr=[]
        min_pen=float(inf)
        for i in range (len(customers)+1):
            min_pen=min(min_pen,count["Y"]+count['N'])
            arr.append(count["Y"]+count['N'])
            if i<len(customers) and customers[i]=="Y":
                count["Y"]-=1
            else:
                count["N"]+=1

        return arr.index(min_pen)