class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7  
        days = n % 7    

        total = 0
        for week in range(weeks):
            for day in range(7):
                total += week + day + 1  
        for day in range(days):
            total += weeks + day + 1  

        return total
