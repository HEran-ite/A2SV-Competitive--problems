class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 10**9 + 7
        def myPow(x, n):
            m = 10**9 + 7

            if n == 0:
                return 1 

            elif n % 2 == 1:
                return (x * myPow((x * x) % m, (n-1) // 2))

            else:
                return myPow((x * x) % m, (n) // 2)

        
        return (myPow(5, n // 2 + n % 2) % m * myPow(4, n//2) % m) % m


        

        
        
    