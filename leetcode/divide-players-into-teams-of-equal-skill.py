class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=len(skill)
        output=0
        total=0
        cur_sum=skill[0]+skill[l-1]
        for i in range(l//2):
            if skill[i]+skill[l-1-i]!= cur_sum:
                return -1
            total+=skill[i]*skill[l-1-i]
        return total