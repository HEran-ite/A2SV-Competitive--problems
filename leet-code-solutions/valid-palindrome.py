class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[]
        s=s.lower()
        for letter in s:
            if letter.isalnum():
                lst.append(letter)
        l,r=0,len(lst)-1
        while l<r:
            if lst[l]==lst[r]:
                l+=1
                r-=1
            else:
                return False
        return True