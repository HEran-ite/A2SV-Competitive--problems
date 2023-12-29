class Solution:
    def smallestNumber(self, num: int) -> int:
        num_str = str(num)
        lst = list(num_str)
        if num >= 0:
            lst.sort()
            if lst[0] == '0':
                for i in range(1, len(lst)):
                    if lst[i] != '0':
                        lst[0], lst[i] = lst[i], lst[0]
                        break
            return int(''.join(lst))
        else:
            lst.remove('-')
            lst.sort(reverse=True)
            return -int(''.join(lst))

        

