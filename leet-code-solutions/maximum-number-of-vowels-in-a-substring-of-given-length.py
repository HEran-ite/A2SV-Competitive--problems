from collections import Counter

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, r = 0, k
        sub_str = s[l:r]
        dic = Counter(sub_str)
        max_vow = 0

        vowels = ['a', 'e', 'i', 'o', 'u']
        count = sum(dic[vowel] for vowel in vowels) 

        max_vow = max(max_vow, count) 

        for r in range(k, len(s)):
            dic[s[l]] -= 1
            dic[s[r]] += 1

            count = sum(dic[vowel] for vowel in vowels)

            max_vow = max(max_vow, count)
            l += 1

        return max_vow
