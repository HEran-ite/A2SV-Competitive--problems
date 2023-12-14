class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        both = set()
        for f, b in zip(fronts, backs):
            if f == b:
                both.add(f)

        goods = []
        for num in fronts + backs:
            if num not in both:
                goods.append(num)

        if not goods:
            return 0
        return min(goods)
