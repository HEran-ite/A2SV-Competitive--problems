class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dire = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    target = board[i][j]
                    target_i, target_j = i, j
                else:
                    continue

                for k in range(9):
                    if target_j == k:
                        continue
                    else:
                        if target == board[i][k]:
                            return False

                for l in range(9):
                    if target_i == l:
                        continue
                    else:
                        if target == board[l][j]:
                            return False

                for n in range(9):
                    for m in range(9):
                        if n == target_i and m == target_j:
                            continue

                        if n // 3 == target_i // 3 and m // 3 == target_j // 3:
                            if target == board[n][m]:
                                return False
        return True
