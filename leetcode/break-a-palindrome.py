class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome)==1:
            return ""
        lst=list(palindrome)
        # print(lst)
        if set(lst[:len(lst)//2])=={'a'}:
            lst.pop()
            lst.append('b')
            return ''.join (lst)
        for i in range (len(lst)):
            if lst[i] !='a':
                lst[i]='a'
                break

        return ''.join (lst)
             
            
