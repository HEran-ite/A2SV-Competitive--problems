class OrderedStream:

    def __init__(self, n: int):
        self.orderedStream = [None] * (n + 1)
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.orderedStream[idKey] = value
        result = []

        if idKey == self.pointer:
            while self.pointer < len(self.orderedStream) and self.orderedStream[self.pointer]:
                result.append(self.orderedStream[self.pointer])
                self.pointer += 1

        return result
