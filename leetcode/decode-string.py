class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = ''
        string = ''
        
        for char in s:
            if char != ']':
                if char.isdigit():
                    num = num + char
                else:
                    if num != '':
                        stack.append(int(num))
                        num = ''
                    stack.append(char)
            else:
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                times = stack.pop()
                result = times * string
                stack.append(result)
                string = ''
                
        return ''.join(stack)

        