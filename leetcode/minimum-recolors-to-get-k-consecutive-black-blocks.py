class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l,r=0,k-1
        min_op=len(blocks)
        while l<=r and r<len(blocks):
            sub_arr=blocks[l:r+1]
            dic=Counter(sub_arr)
            count=dic['W']
            min_op=min(min_op,count)
            r+=1
            l+=1
        return min_op

