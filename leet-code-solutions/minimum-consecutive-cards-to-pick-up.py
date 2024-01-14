from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        card_index = {}
        min_consecutive = float('inf')
        for i, card in enumerate(cards):
            if card in card_index:
                min_consecutive = min(min_consecutive, i - card_index[card] + 1)
            card_index[card] = i

        return min_consecutive if min_consecutive != float('inf') else -1

