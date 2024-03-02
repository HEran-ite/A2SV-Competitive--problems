class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue=deque()
        for num in deck:
            if len(queue)>=2:
                queue.appendleft(queue.pop())
            queue.appendleft(num)

        return queue


            
