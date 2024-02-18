class RecentCounter:

    def __init__(self):
        self.counter=0
        self.stack=[]
    def ping(self, t: int) -> int:
        while len(self.stack) and t-self.stack[0]>3000:
            self.stack.remove(self.stack[0])
        self.stack.append(t)
        return len(self.stack)
        

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)