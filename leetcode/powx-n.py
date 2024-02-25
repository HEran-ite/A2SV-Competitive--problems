class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1 
        
        
        elif n < 0 :

            return 1/( x * self.myPow(x,-n-1)) 


        elif n % 2 == 0:

            binary = self.myPow(x, n // 2)
            return binary * binary
            
        return x * self.myPow(x, n - 1)