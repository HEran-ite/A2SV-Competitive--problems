class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        stack = []
        m = 10**9 + 7
        for i in range(len(arr)):
            while stack and arr[i] < stack[-1][0]:
                val, idx = stack.pop()
                if stack:
                    l = idx - stack[-1][1]
                else:
                    l = idx + 1

                r = i - idx
                res += val * l * r
                res %= m  

            stack.append([arr[i], i])

        # Process the remaining elements in the stack
        while stack:
            val, idx = stack.pop()
            if stack:
                l = idx - stack[-1][1]
            else:
                l = idx + 1
            r = len(arr) - idx
            res += val * l * r
            res %= m 

        return res
