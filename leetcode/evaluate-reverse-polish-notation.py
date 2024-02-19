class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=0
        stack=[]
        op = {"+": lambda x, y: x + y,"-": lambda x, y: x - y,"*": lambda x, y: x * y,"/": lambda x, y: x / y}
        if len(tokens)==1:
            return int(tokens[0])
        for num in tokens:
            if num not in op.keys():
                stack.append(num)

            else:
                   n2=stack.pop()
                   n1=stack.pop()
                   stack.append(int(op[num](int(n1),int(n2))))

        return stack[0]