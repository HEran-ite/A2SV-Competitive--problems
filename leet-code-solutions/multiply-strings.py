class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m = len(num1)
        n = len(num2)
        result = [0] * (m + n)
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos1 = i + j
                pos2 = i + j + 1
                sum = mul + result[pos2]
                
                result[pos2] = sum % 10
                result[pos1] += sum // 10
        
        res = ""
        for digit in result:
            if not (res == "" and digit == 0):
                res += str(digit)
        
        return res


