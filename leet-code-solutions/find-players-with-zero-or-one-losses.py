class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners = {}
        losers = {}
        no_lose = []
        one_lose = []
        
        for match in matches:
            if match[0] in winners:
                winners[match[0]] += 1
            else:
                winners[match[0]] = 1
                
            if match[1] in losers:
                losers[match[1]] += 1
            else:
                losers[match[1]] = 1
                
        for winner in winners:
            if winner not in losers:
               no_lose.append(winner)
        
        for loser in losers:
            if losers[loser] == 1:
                one_lose.append(loser)
        
        no_lose.sort()
        one_lose.sort()
        
        return [no_lose, one_lose]
            

                



                
            