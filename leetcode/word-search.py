from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        path = set()

        def helper(r, c, idx):
            if idx == len(word):  
                return True
            if not (0 <= r < row) or not (0 <= c < col) or word[idx] != board[r][c] or (r, c) in path:
                return False
            path.add((r, c))

            res = (helper(r + 1, c, idx + 1) or helper(r - 1, c, idx + 1) or
                   helper(r, c + 1, idx + 1) or helper(r, c - 1, idx + 1))

            path.remove((r, c))
            return res

        for i in range(row):
            for j in range(col):
                if helper(i, j, 0):
                    return True
        return False
