from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.data = []
        for item in combinations(list(characters), combinationLength):
            self.data.append("".join(c for c in item))
        self.length = len(self.data)

    def next(self) -> str:
        self.length -= 1
        return str(self.data.pop(0))


    def hasNext(self) -> bool:
        return True if self.length > 0 else False

# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("abc", 2)
param_1 = obj.next()
print(param_1)
param_2 = obj.hasNext
print(param_2)