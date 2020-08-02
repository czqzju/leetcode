
class MyHashSet:

    def __init__(self):
        self.data = set()

    def add(self, key: int) -> None:
        self.data.add(key)

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.data

# Your MyHashSet object will be instantiated and called as such:
key = 3
obj = MyHashSet()
obj.add(key)
obj.remove(key)
param_3 = obj.contains(key)