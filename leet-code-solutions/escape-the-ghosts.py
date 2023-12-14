class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist=abs(target[0])+abs(target[1])
        for i in range(len(ghosts)):
            s=abs(ghosts[i][0]-target[0])+abs(ghosts[i][1]-target[1])
            if s<=dist:
                return False
        return True
        