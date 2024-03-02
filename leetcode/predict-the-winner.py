class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def backtrack(l, r):
            if l > r:
                return 0, 0
            
            curr1, nxt1 = backtrack(l+1, r)
            curr2, nxt2 = backtrack(l, r-1)
                        
            if nums[l] + nxt1 > nums[r] + nxt2:
                return nums[l] + nxt1, curr1
            
            return nums[r] + nxt2, curr2
        
        player1, player2 = backtrack(0, len(nums)-1)
        
        return player1 >= player2