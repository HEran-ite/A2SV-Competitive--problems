class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        state = [[0] * n for i in range(m)]
        count = 0
        g = 1
        w = 2
        used = 3

        
        for i, j in guards:
            state[i][j] = g

 
        for i, j in walls:
            state[i][j] = w

  
        for i in range(m):
            curr = 0
            for j in range(n):  # Left to right
                if state[i][j] == g:
                    curr = used
                elif state[i][j] == w:
                    curr = 0
                elif curr == used:
                    state[i][j] = used

            curr = 0
            for j in range(n-1, -1, -1):  # Right to left
                if state[i][j] == g:
                    curr = used
                elif state[i][j] == w:
                    curr = 0
                elif curr == used:
                    state[i][j] = used

        
        for j in range(n):
            curr = 0
            for i in range(m):  # Top to bottom
                if state[i][j] == g:
                    curr = used
                elif state[i][j] == w:
                    curr = 0
                elif curr == used:
                    state[i][j] = used

            curr = 0
            for i in range(m-1, -1, -1):  # Bottom to top
                if state[i][j] == g:
                    curr = used
                elif state[i][j] == w:
                    curr = 0
                elif curr == used:
                    state[i][j] = used


        for i in range(m):
            for j in range(n):
                if state[i][j] == 0:
                    count += 1
        return count
