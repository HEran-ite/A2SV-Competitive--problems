class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count= 0

        for bracket in s:
            if bracket == '(':
                stack.append(count)
                count = 0
            else:
                count = stack.pop() + max(2 * count, 1)
        return count
            