class Bitset:

    def __init__(self, size: int):
        self.bitset = [0] * size
        self.bitset2 = [1] * size
        self.set_bits_count = 0 
        self.size = size

    def fix(self, idx: int) -> None:
        if self.bitset[idx] != 1:
            self.bitset[idx] = 1
            self.bitset2[idx] = 0
            self.set_bits_count += 1

    def unfix(self, idx: int) -> None:
        if self.bitset[idx] != 0:
            self.bitset[idx] = 0
            self.bitset2[idx] = 1
            self.set_bits_count -= 1

    def flip(self) -> None:
        self.bitset, self.bitset2 = self.bitset2, self.bitset
        self.set_bits_count = self.size - self.set_bits_count

    def all(self) -> bool:
        return self.set_bits_count == self.size

    def one(self) -> bool:
        return self.set_bits_count > 0

    def count(self) -> int:
        return self.set_bits_count

    def toString(self) -> str:
        return ''.join(str(bit) for bit in self.bitset)
