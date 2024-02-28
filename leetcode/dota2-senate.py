class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad=deque()
        dire=deque()
        n=len(senate)
        for i in range (len(senate)):
            if senate[i]=='R':
                rad.append(i)
            else:
                dire.append(i)
        while rad and dire:
            if dire.popleft() < rad.popleft():
                dire.append(n)
            else:
                rad.append(n)
            n+=1
        if not rad:
            return 'Dire'
        return 'Radiant'
                