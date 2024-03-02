class BrowserHistory:

    def __init__(self, homepage: str):
        self.fStack=[]
        self.bStack=[homepage]

    def visit(self, url: str) -> None:
        self.bStack.append(url)
        self.fStack=[]

    def back(self, steps: int) -> str:
        if len(self.bStack)<steps:
            while len(self.bStack)>1:
                self.fStack.append(self.bStack.pop())
            return self.bStack[-1]
        else:
            while len(self.bStack)>1 and steps>0 :
                self.fStack.append(self.bStack.pop())
                steps-=1
            return self.bStack[-1]

    def forward(self, steps: int) -> str:
        if len(self.fStack)<steps:
            while len(self.fStack):
                self.bStack.append(self.fStack.pop())
            return self.bStack[-1]
        else:
            while len(self.fStack) and steps>0:
                self.bStack.append(self.fStack.pop())
                steps-=1
            return self.bStack[-1]


        # if len(self.fStack)<steps:
        #     return self.fStack[0]
        # self.bStack.append(self.fStack.pop())
        # return self.bStack[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)