class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dicT=Counter(t)
        dicS=defaultdict(int)
        min_count=float(inf)
        have,need=0,len(dicT)
        l,real_l,real_r=0,0,0

        if t =='':
            return ''
        for r in range(len(s)):

            dicS[s[r]]+=1

            if s[r] in dicT and dicS[s[r]]==dicT[s[r]]:
                have+=1

            while have == need:

                if (r-l+1) < min_count:
                    real_l=l
                    real_r=r
                    min_count=r-l+1

                dicS[s[l]]-=1

                if s[r] in dicT and dicS[s[l]] < dicT[s[l]]:
                    have-=1

                l+=1
        if min_count==float(inf):
            return ''
        return s[real_l:real_r+1]

            

