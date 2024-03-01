import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
    

        if n & (n - 1) != 0:
            return False


        return math.log2(n) % 2 == 0