class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(l, k):
            if l == 1:
                return 0
            prev = 2**(l - 2)
            if k <= prev:
                return helper(l - 1, k)
            else:
                return 1 - helper(l - 1, k - prev)

        return helper(n, k)



        