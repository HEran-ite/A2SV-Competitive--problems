import random

class RandomizedSet:

    def __init__(self):
        self.randomizedSet = []
        self.valToIndex = {}

    def insert(self, val: int) -> bool:
        if val in self.valToIndex:
            return False
        else:
            self.randomizedSet.append(val)
            self.valToIndex[val] = len(self.randomizedSet) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.valToIndex:
            index = self.valToIndex[val]
            last_val = self.randomizedSet[-1]

            self.randomizedSet[index] = last_val
            self.valToIndex[last_val] = index

            self.randomizedSet.pop()
            del self.valToIndex[val]
            
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.randomizedSet)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()